import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Replace these with your actual Spotify API credentials
client_id = "4ffd38f41a664bad9150c3774ad3734a"
client_secret = "09792ab70fe24a648836b7dd18a9dce8"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Load your dataset
file_path = '/Users/pranalidarekar/Downloads/spotify-2023.csv'
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Function to get the album cover URL
def get_album_cover_url(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    result = sp.search(query, type='track', limit=1)
    if result['tracks']['items']:
        return result['tracks']['items'][0]['album']['images'][0]['url']
    return None

# Apply the function to each row in the dataset
spotify_data['album_cover_url'] = spotify_data.apply(
    lambda row: get_album_cover_url(row['track_name'], row['artist(s)_name']), axis=1
)

# Save the updated dataset with album cover URLs
updated_file_path = '/Users/pranalidarekar/Downloads/spotify-2023.csv'
spotify_data.to_csv(updated_file_path, index=False)

# Display the first few rows of the updated dataset
spotify_data.head()
