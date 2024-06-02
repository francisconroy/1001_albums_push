from unittest import TestCase

from albumgenerator import clean_username, extract_album_data


class TestCleanUsername(TestCase):
    def test_clean_username(self):
        self.assertEqual("test-user", clean_username("Test User"))
        self.assertEqual("test-ralph-user", clean_username("Test Ralph User"))


class TestExtractAlbumData(TestCase):
    def setUp(self):
        self.sample_data = {
            'shareableUrl': 'https://1001albumsgenerator.com/shares/6656bf590b5c7a12647e0009',
            'currentAlbum': {'artist': 'Yeah Yeah Yeahs', 'artistOrigin': 'us',
                             'images': [{'height': 634,
                                         'url': 'https://i.scdn.co/image/4b288e03ec8c7739000756bbeea48b732dd49825',
                                         'width': 640}, {'height': 297,
                                                         'url': 'https://i.scdn.co/image/d6c65eae8f038f0e85323a7c9f686283c72b2727',
                                                         'width': 300},
                                        {'height': 63,
                                         'url': 'https://i.scdn.co/image/32d66005dadb1c5c2c8fb109ac39a0178a7cc28a',
                                         'width': 64}],
                             'genres': ['rock', 'punk', 'indie'],
                             'subGenres': ['alternative-dance',
                                           'alternative-rock', 'dance-punk',
                                           'garage-rock', 'indie-rock',
                                           'modern-rock', 'new-rave', 'rock'],
                             'name': 'Fever To Tell', 'slug': 'fever-to-tell',
                             'releaseDate': '2003',
                             'globalReviewsUrl': 'https://1001albumsgenerator.com/albums/4DEZVbAxlZPRXWCHUV5wF3/fever-to-tell',
                             'wikipediaUrl': 'https://en.wikipedia.org/wiki/Fever_to_Tell',
                             'spotifyId': '4DEZVbAxlZPRXWCHUV5wF3',
                             'appleMusicId': '1440916724', 'tidalId': 79976111,
                             'amazonMusicId': 'B07GJN49YC',
                             'youtubeMusicId': 'OLAK5uy_nIIg5KyBqnM6MleAyCNhOkwDDBe3RqEaI',
                             'qobuzId': '0060256703166',
                             'deezerId': '49844632'}, 'currentAlbumNotes': '',
            'history': [{'album': {'artist': 'Fela Kuti',
                                   'artistOrigin': 'other', 'images': [
                    {'height': 640,
                     'url': 'https://i.scdn.co/image/d4b0965648540545e81310d12609eb59788a4f98',
                     'width': 640}, {'height': 300,
                                     'url': 'https://i.scdn.co/image/bf1faa1ed75c701fffb89dd008df00494aed0880',
                                     'width': 300}, {'height': 64,
                                                     'url': 'https://i.scdn.co/image/bdcbdeab40e1667ef9773f87e899d6cc506c4d2b',
                                                     'width': 64}],
                                   'genres': ['funk', 'soul', 'world'],
                                   'subGenres': ['afrobeat', 'afropop', 'funk',
                                                 'world'], 'name': 'Live!',
                                   'slug': 'live', 'releaseDate': '1971',
                                   'globalReviewsUrl': 'https://1001albumsgenerator.com/albums/4YYW1Q1okABRHpSj6LMtEO/live',
                                   'wikipediaUrl': 'https://en.wikipedia.org/wiki/Live!_(Fela_Kuti_album)',
                                   'spotifyId': '4YYW1Q1okABRHpSj6LMtEO',
                                   'appleMusicId': '682949290',
                                   'tidalId': 18773791,
                                   'youtubeMusicId': 'OLAK5uy_nFM5GFOCEVMfIBZLtLk5Otorsj9ga8ckU',
                                   'qobuzId': '5051083068567',
                                   'deezerId': '6273647'}, 'rating': 5,
                         'review': 'Wonderful. I’d heard nothing like it before. ',
                         'generatedAt': '2024-05-29T03:00:58.068Z',
                         'globalRating': 3.46}, {
                            'album': {'artist': 'War', 'artistOrigin': 'us',
                                      'images': [{'height': 640,
                                                  'url': 'https://i.scdn.co/image/ab67616d0000b27362f7c579da4d8219a0f81bf1',
                                                  'width': 640}, {'height': 300,
                                                                  'url': 'https://i.scdn.co/image/ab67616d00001e0262f7c579da4d8219a0f81bf1',
                                                                  'width': 300},
                                                 {'height': 64,
                                                  'url': 'https://i.scdn.co/image/ab67616d0000485162f7c579da4d8219a0f81bf1',
                                                  'width': 64}],
                                      'genres': ['soul', 'funk'],
                                      'subGenres': ['classic-soul', 'funk',
                                                    'quiet-storm', 'soul'],
                                      'name': 'The World is a Ghetto',
                                      'slug': 'the-world-is-a-ghetto',
                                      'releaseDate': '1972',
                                      'globalReviewsUrl': 'https://1001albumsgenerator.com/albums/4UZmpGH8kpAgyZ2yqQ8sP9/the-world-is-a-ghetto',
                                      'wikipediaUrl': 'https://en.wikipedia.org/wiki/The_World_Is_a_Ghetto',
                                      'spotifyId': '4UZmpGH8kpAgyZ2yqQ8sP9',
                                      'appleMusicId': '1202363758',
                                      'tidalId': 70046659,
                                      'amazonMusicId': 'B073JMF9WQ',
                                      'youtubeMusicId': 'OLAK5uy_kNA_XtmrSxrdSuwLmfS-bgfhJBYTUcPTk',
                                      'qobuzId': '0602527595092',
                                      'deezerId': '15484166'}, 'rating': 4,
                            'review': '',
                            'generatedAt': '2024-05-30T03:00:54.218Z',
                            'globalRating': 3.34}], 'updateFrequency': 'daily',
            'name': 'Redacted'}

    def test_extract_album_data(self):
        ad = extract_album_data(self.sample_data)
        self.assertEqual(ad.spotify_id, '4DEZVbAxlZPRXWCHUV5wF3')
        self.assertEqual(ad.album_name, 'Fever To Tell')
        self.assertEqual(ad.album_artist, 'Yeah Yeah Yeahs')
        self.assertEqual(ad.album_release, '2003')
        self.assertEqual(ad.cover_url, 'https://i.scdn.co/image/32d66005dadb1c5c2c8fb109ac39a0178a7cc28a')
        self.assertEqual(ad.spotify_url, 'spotify:album:4DEZVbAxlZPRXWCHUV5wF3')
        pass
