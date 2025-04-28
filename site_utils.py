# site_utils.py

import pandas as pd
import os
import requests
import zipfile
import geopandas as gpd
from shapely.geometry import Point


# Fuction that downloads and extracts the shapefile
def download_and_extract_shapefile(zip_url, output_dir, zip_name="data.zip"):
    """
    Downloads and extracts a ZIP file from a URL containing shapefiles,
    then returns the first .shp file as a GeoDataFrame.

    Parameters:
    - zip_url (str): The URL to the ZIP file.
    - output_dir (str): The local directory where data should be stored.
    - zip_name (str): Optional name for the downloaded ZIP file.

    Returns:
    - GeoDataFrame: Loaded from the first shapefile in the extracted contents.
    """
    os.makedirs(output_dir, exist_ok=True)
    zip_path = os.path.join(output_dir, zip_name)

    # Download if ZIP doesn't exist
    if not os.path.exists(zip_path):
        print(f"Downloading data from {zip_url}...")
        response = requests.get(zip_url)
        response.raise_for_status()  # Will raise an error for bad status codes
        with open(zip_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")

        # Unzip the file
        print("Extracting contents...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print("Extraction complete.")

    # Locate the shapefile
    shapefile_path = None
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".shp"):
                shapefile_path = os.path.join(root, file)
                break
        if shapefile_path:
            break

    if shapefile_path is None:
        raise FileNotFoundError("No .shp file found in the extracted archive.")

    print(f"Shapefile found: {shapefile_path}")
    return gpd.read_file(shapefile_path)


def plot_fire_boundary(gdf, fire_name, fire_column='Incid_Name', title=None):
    """
    Filters a GeoDataFrame for a specific fire and plots its boundary.

    Parameters:
    - gdf (GeoDataFrame): The input GeoDataFrame with fire perimeters.
    - fire_name (str): The name of the fire to filter by (case sensitive).
    - fire_column (str): The name of the column containing fire names. Default is 'Incid_Name'.
    - title (str, optional): Title for the plot. If None, it defaults to 'Fire Parameter: {fire_name}'.

    Returns:
    - hvplot: An interactive plot of the fire boundary.
    """
    # Filter
    fire_gdf = gdf[gdf[fire_column] == fire_name]

    if fire_gdf.empty:
        raise ValueError(f"No fire found with name '{fire_name}' in column '{fire_column}'.")

    # Dissolve geometries if needed
    dissolved = fire_gdf.dissolve()

    # Title
    plot_title = title or f'Fire Parameter: {fire_name}'

    # Plot
    return dissolved.hvplot(
        geo=True,
        tiles='EsriImagery',
        title=plot_title,
        fill_color=None,
        line_color='red',
        line_width=1,
        frame_width=600
    )


def load_csv_data(csv_filename, base_dir, header='infer', names=None):
    """
    Loads a CSV file from a given base directory with a flexible header and column name option.
    
    Parameters:
        csv_filename (str): Name of the CSV file (e.g., 'fire_stats.csv')
        base_dir (str): Directory path where the file lives
        header (int, str, or None): Row to use as column names, or None if no headers.
        names (list, optional): List of column names to use if header is None.
        
    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    csv_path = os.path.join(base_dir, csv_filename)

    try:
        df = pd.read_csv(csv_path, header=header, names=names)
        print(f"✅ Loaded '{csv_filename}' with {len(df)} rows and {len(df.columns)} columns.")
        return df
    except Exception as e:
        print(f"⚠️ Could not load '{csv_filename}': {e}")
        return None
