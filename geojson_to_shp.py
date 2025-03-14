# prompt: write a python code to convert geojson to shp

import geopandas as gpd
import json
import os

def geojson_to_shp(geojson_file, shp_file):
    """Converts a GeoJSON file to a Shapefile.

    Args:
        geojson_file: Path to the input GeoJSON file.
        shp_file: Path to the output Shapefile.
    """
    try:
        # Read the GeoJSON file into a GeoDataFrame
        gdf = gpd.read_file(geojson_file)

        # Write the GeoDataFrame to a Shapefile
        gdf.to_file(shp_file)

        print(f"Successfully converted {geojson_file} to {shp_file}")

    except FileNotFoundError:
        print(f"Error: GeoJSON file not found at {geojson_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage (assuming you have a 'data.geojson' file)
# geojson_to_shp('data.geojson', 'output.shp')

geojson_file = r"E:\UAH_Classes\AES_515\Assignment_II\Service_Area_Analysis\SanDiego\Data\Buildings\California\California.geojson"

# Example with in-memory GeoJSON data:
geojson_data = gpd.read_file(geojson_file)

# Convert in-memory GeoJSON to a GeoDataFrame
gdf_from_dict = gpd.GeoDataFrame.from_features(geojson_data)

# Save to shapefile (replace 'output_from_dict.shp' with your desired filename)
gdf_from_dict.to_file('output_from_dict.shp')
print(os.getcwd())