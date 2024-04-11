import unittest
from project.social_media import SocialMedia


class SocialMediaTests(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia("ExtremelyFamous123",
                                        "YouTube", 1000000, "VideoGaming")

    def test_social_media_initialization(self):
        self.assertEqual("ExtremelyFamous123", self.social_media._username)
        self.assertEqual("YouTube", self.social_media._platform)
        self.assertEqual(1000000, self.social_media._followers)
        self.assertEqual("VideoGaming", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_validate_and_set_platform_allowed_platform(self):
        self.social_media.platform = "Instagram"
        self.assertEqual("Instagram", self.social_media._platform)

    def test_validate_and_set_platform_not_allowed_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "Twitch"

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))
        self.assertEqual("YouTube", self.social_media._platform)

    def test_followers_setter_positive_value(self):
        self.social_media.followers = 2000000
        self.assertEqual(2000000, self.social_media._followers)

    def test_followers_setter_zero_value(self):
        self.social_media.followers = 0
        self.assertEqual(0, self.social_media._followers)

    def test_followers_setter_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -500
        self.assertEqual("Followers cannot be negative.", str(ve.exception))
        self.assertEqual(1000000, self.social_media._followers)

    def test_create_post_method_one_post(self):
        result = self.social_media.create_post("League of Legends URF")
        self.assertEqual("New VideoGaming post created by ExtremelyFamous123 on YouTube.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': []}], self.social_media._posts)

    def test_create_post_method_a_lot_of_posts(self):
        result = self.social_media.create_post("League of Legends URF")
        self.assertEqual("New VideoGaming post created by ExtremelyFamous123 on YouTube.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': []}], self.social_media._posts)

        result = self.social_media.create_post("CS:GO Good Old Days")
        self.assertEqual("New VideoGaming post created by ExtremelyFamous123 on YouTube.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []}], self.social_media._posts)

        result = self.social_media.create_post("NEW RIOT GAMES GAME REACTION")
        self.assertEqual("New VideoGaming post created by ExtremelyFamous123 on YouTube.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}], self.social_media._posts)

    def test_like_post_method_no_posts(self):
        result = self.social_media.like_post(0)
        self.assertEqual("Invalid post index.", result)
        self.assertEqual([], self.social_media._posts)

    def test_like_post_method_invalid_index(self):
        self.social_media.create_post("League of Legends URF")
        result = self.social_media.like_post(2)
        self.assertEqual("Invalid post index.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': []}], self.social_media._posts)

    def test_like_post_method_more_than_one_post(self):
        self.social_media.create_post("League of Legends URF")
        self.social_media.create_post("CS:GO Good Old Days")
        self.social_media.create_post("NEW RIOT GAMES GAME REACTION")

        result = self.social_media.like_post(0)
        self.assertEqual("Post liked by ExtremelyFamous123.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 1, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.like_post(0)
        self.assertEqual("Post liked by ExtremelyFamous123.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 2, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.like_post(1)
        self.assertEqual("Post liked by ExtremelyFamous123.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 2, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 1, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.like_post(2)
        self.assertEqual("Post liked by ExtremelyFamous123.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 2, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 1, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 1, 'comments': []}],
                         self.social_media._posts)

    def test_like_post_method_maximum_likes(self):
        self.social_media.create_post("League of Legends URF")
        self.social_media.create_post("CS:GO Good Old Days")
        self.social_media.create_post("NEW RIOT GAMES GAME REACTION")

        for i in range(10):
            result = self.social_media.like_post(0)
            self.assertEqual("Post liked by ExtremelyFamous123.", result)
            self.assertEqual([{'content': "League of Legends URF", 'likes': i+1, 'comments': []},
                              {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                              {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                             self.social_media._posts)

        result = self.social_media.like_post(1)
        self.assertEqual("Post liked by ExtremelyFamous123.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 10, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 1, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 10, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 1, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.like_post(1)
        self.assertEqual("Post liked by ExtremelyFamous123.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 10, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 2, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

    def test_comment_on_post_method_small_comment(self):
        self.social_media.create_post("League of Legends URF")
        self.social_media.create_post("CS:GO Good Old Days")
        self.social_media.create_post("NEW RIOT GAMES GAME REACTION")

        result = self.social_media.comment_on_post(0, "FIRST")
        self.assertEqual("Comment should be more than 10 characters.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': []},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

    def test_comment_on_post_method_one_comment_per_post(self):
        self.social_media.create_post("League of Legends URF")
        self.social_media.create_post("CS:GO Good Old Days")
        self.social_media.create_post("NEW RIOT GAMES GAME REACTION")

        result = self.social_media.comment_on_post(0, "This video is great! I <3 it.")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0, 'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.comment_on_post(1, "Not your type of content, but I do enjoy it!")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "Not your type of content, but I do enjoy it!"}]},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.comment_on_post(2, "The game sounds interesting! Waiting...")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123",
                                         'comment': "Not your type of content, but I do enjoy it!"}]},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': [{'user': "ExtremelyFamous123",
                                         'comment': "The game sounds interesting! Waiting..."}]}],
                         self.social_media._posts)

    def test_comment_on_post_method_a_lot_of_comments(self):
        self.social_media.create_post("League of Legends URF")
        self.social_media.create_post("CS:GO Good Old Days")
        self.social_media.create_post("NEW RIOT GAMES GAME REACTION")

        result = self.social_media.comment_on_post(0, "This video is great! I <3 it.")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.comment_on_post(0, "Not your type of content, but I do enjoy it!")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."},
                                        {'user': "ExtremelyFamous123", 'comment': "Not your type of content, but I do enjoy it!"}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.comment_on_post(0, "The game sounds interesting! Waiting...")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."},
                                        {'user': "ExtremelyFamous123",
                                         'comment': "Not your type of content, but I do enjoy it!"}, {'user': "ExtremelyFamous123",
                                         'comment': "The game sounds interesting! Waiting..."}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': []},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

        result = self.social_media.comment_on_post(1, "Spicy new video!!!!! Waiting for next one!")
        self.assertEqual("Comment added by ExtremelyFamous123 on the post.", result)
        self.assertEqual([{'content': "League of Legends URF", 'likes': 0,
                           'comments': [{'user': "ExtremelyFamous123", 'comment': "This video is great! I <3 it."},
                                        {'user': "ExtremelyFamous123",
                                         'comment': "Not your type of content, but I do enjoy it!"},
                                        {'user': "ExtremelyFamous123",
                                         'comment': "The game sounds interesting! Waiting..."}]},
                          {'content': "CS:GO Good Old Days", 'likes': 0, 'comments': [{'user': "ExtremelyFamous123",
                                         'comment': "Spicy new video!!!!! Waiting for next one!"}]},
                          {'content': "NEW RIOT GAMES GAME REACTION", 'likes': 0, 'comments': []}],
                         self.social_media._posts)

if __name__ == "__main__":
    unittest.main()
