import media
import fresh_tomatoes

toyStory = media.Movie("Toy Story",
"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avatar = media.Movie("Avatar",
"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=xy1ccIP_i24")

hunter_killer = media.Movie("Hunter Killer",
"An untested American submarine captain teams with U.S. Navy Seals to rescue the Russian president, who has been kidnapped by a rogue general.",
"https://upload.wikimedia.org/wikipedia/en/6/63/Hunter_Killer_film_poster.jpg",
"https://www.youtube.com/watch?v=QAhcDHRZOak")

EqualizerII = media.Movie("Equalizer II",
"Robert McCall serves an unflinching justice for the exploited and oppressed, but how far will he go when that is someone he loves?",
"https://upload.wikimedia.org/wikipedia/en/7/73/The_Equalizer_2_poster.jpg",
"https://www.youtube.com/watch?v=HyNJ3UrGk_I")

mile22 = media.Movie("Mile 22",
"An elite American intelligence officer, aided by a top-secret tactical command unit, tries to smuggle a mysterious police officer with sensitive information out of Indonesia.",
"https://upload.wikimedia.org/wikipedia/en/4/41/Mile_22.png",
"https://www.youtube.com/watch?v=eJU6S5KOsNI")

alpha = media.Movie("Alpha",
"In the prehistoric past, a young man struggles to return home after being separated from his tribe during a buffalo hunt. He finds a similarly lost wolf companion and starts a friendship that would change humanity.",
"https://m.media-amazon.com/images/M/MV5BODI4OTk1ODY3N15BMl5BanBnXkFtZTgwMDI1MTcwNjM@._V1_.jpg",
"https://www.youtube.com/watch?v=uIxnTi4GmCo")


movies = [toyStory, avatar, hunter_killer, EqualizerII, mile22, alpha]

fresh_tomatoes.open_movies_page(movies)
