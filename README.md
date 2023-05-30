FORMAT: 1A
HOST: https://13.234.60.82/
# Collabo 
http://13.234.60.82/api/order/
#domain=in

## 1. Cities List
http://13.234.60.82/api/cities/?domain=in
Response
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "state": {
                "id": 1,
                "name": "Kerala"
            },
            "name": "Kochi",
            "short_name": "cochin",
            "slug": "kochi-kerala"
        }
    ]
}
## 2. Event List
http://13.234.60.82/api/eventlists/?city=kochi&domain=in
Response
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Shreya Ghoshal Live in Concert",
            "short_title": null,
            "slug": "shreya-ghoshal-live-in-concert",
            "ticket_type": "Multiple Ticket",
            "start_time": "2019-05-10T17:30:41.000000Z",
            "end_time": "2019-05-11T22:30:56.000000Z",
            "city": {
                "name": "Kochi",
                "short_name": "KOK",
                "slug": "kochi",
                "payment_method": "PAYTM"
            },
            "booking": {
                "type": "Bookable",
                "button_text": "Book Now",
                "external_url": "None"
            },
            "category": {
                "category_id": 1,
                "name": "Music Show",
                "slug": "music-show",
                "weight": 1
            },
            "address_venue": {
                "title": "Crowne Plaza Kochi",
                "label": "",
                "capacity": 150,
                "rate": 123,
                "about": "<p><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span></p>",
                "type": {
                    "id": 1,
                    "title": "Resort"
                },
                "upload": [
                    {
                        "id": 1,
                        "image_name": "image1",
                        "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                    }
                ],
                "location": {
                    "place": "Crowne Plaza Kochi, Kundannoor, Junction, Kochi, Kerala, India",
                    "latitude": 9.9341165,
                    "longitude": 76.31893739999998
                },
                "slug": "crowne-plaza-kochi",
                "city": {
                    "name": "Kochi",
                    "short_name": "KOK",
                    "slug": "kochi",
                    "payment_method": "PAYTM"
                }
            },
            "lowest_price": 0
        }
    ]
}

## 3. Venue List
http://13.234.60.82/api/venuelists/?city=kochi&domain=in
Response
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Crowne Plaza Kochi",
            "label": "",
            "capacity": 150,
            "rate": 123,
            "about": "<p><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span></p>",
            "type": {
                "id": 1,
                "title": "Resort"
            },
            "upload": [
                {
                    "id": 1,
                    "image_name": "image1",
                    "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                }
            ],
            "location": {
                "place": "Crowne Plaza Kochi, Kundannoor, Junction, Kochi, Kerala, India",
                "latitude": 9.9341165,
                "longitude": 76.31893739999998
            }
        }
    ]
}



##4 Artists Lists
http://13.234.60.82/api/artistlists?city=kochi&domain=in
Resonse
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "artistImage": [
                {
                    "id": 2,
                    "image_name": "shreya1",
                    "upload": "http://13.234.60.82/media/ArtistPhotos/shreya1/p05f6tb3.jpg"
                },
                {
                    "id": 3,
                    "image_name": "shreya2",
                    "upload": "http://13.234.60.82/media/ArtistPhotos/shreya2/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                }
            ],
            "artistSong": [],
            "title": "Shreya Ghoshal",
            "thumbnail": null,
            "slug": "shreya-ghoshal",
            "fb_followers": 2500,
            "inst_followers": null,
            "rate": null,
            "about": "<p><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">Playback singer Shreya Ghoshal started her illustrious career in 2002 after she was noticed by Sanjay Leela Bhansali when she won the musical reality show Sa Re Ga Ma Pa at the age of sixteen and subsequently sang five songs in his film, Devdas. Her seductive numbers in Jism established her as a versatile singer in the industry, and since then she has only seen progress in her career. Working with big names in the industry, like Anu Malik, Shankar-Ehsaan-Loy, Nadeem-Shravan she lent her voice to popular songs like Piyu Bole, Dheere Jalna, Agar Tum Mil Jao, Pehle Se, Hum To Aise Hain, Yeh Ishq Haaye, Mere Dholna, Main Agar Kahoon, Deewani Mastani, Pinga among many more, before she was associated with Bucket List (2018). Her other 2018 releases include Padmaavat, Sanju and Dhadak.&nbsp;</span><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">A recipient of four National Film Awards and six Filmfare Awards, Shreya became the first Indian singer to get a wax statue in the Indian Madame Tussauds. Apart from Hindi cinema, she is widely known for her songs in the South Indian film industry as well, like Yen Chellam in Album (2002), Munbe Vaa composed by A. R. Rahman, for which she bagged the Tamil Nadu State Film Award. She has also appeared in several musical reality TV shows. Ted Strickland, the governor of Ohio declared 26 June as 'Shreya Ghoshal Day'. She was awarded the highest honour in London by the members of House of Commons of the United Kingdom on April 2013.</span></p>",
            "city": 1
        },
        {
            "id": 1,
            "artistImage": [
                {
                    "id": 1,
                    "image_name": "ar rahman",
                    "upload": "http://13.234.60.82/media/ArtistPhotos/ar%20rahman/ar_rahman.jpeg"
                }
            ],
            "artistSong": [
                {
                    "id": 1,
                    "image_name": "A. R. Rahman Meets Berklee - V",
                    "upload": "https://www.youtube.com/watch?v=Ss-kLGW2pHQ"
                }
            ],
            "title": "AR Rahman",
            "thumbnail": null,
            "slug": "ar-rahman",
            "fb_followers": 1234,
            "inst_followers": 1235,
            "rate": 124,
            "about": "<p style=\"margin: 0.5em 0px; line-height: inherit; color: #222222; font-family: sans-serif;\"><strong>Allahrakka Rahman</strong>&nbsp;(<span class=\"unicode haudio\"><span class=\"fn\"><span style=\"white-space: nowrap; margin-right: 0.25em;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"About this sound\" href=\"https://en.wikipedia.org/wiki/File:A_R_Rahman.ogg\"><img style=\"border: 0px; vertical-align: middle; margin: 0px;\" src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x\" alt=\"About this sound\" width=\"11\" height=\"11\" data-file-width=\"20\" data-file-height=\"20\" /></a></span><a class=\"internal\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"A R Rahman.ogg\" href=\"https://upload.wikimedia.org/wikipedia/commons/9/9c/A_R_Rahman.ogg\">pronunciation</a></span>&nbsp;<small class=\"metadata audiolinkinfo\" style=\"font-size: 11.9px; cursor: help;\">(<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Wikipedia:Media help\" href=\"https://en.wikipedia.org/wiki/Wikipedia:Media_help\"><span style=\"cursor: help;\">help</span></a>&middot;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"File:A R Rahman.ogg\" href=\"https://en.wikipedia.org/wiki/File:A_R_Rahman.ogg\"><span style=\"cursor: help;\">info</span></a>)</small></span>; born&nbsp;<strong>A. S. Dileep Kumar</strong>) known professionally as&nbsp;<strong>A. R. Rahman</strong>, is an&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Indian people\" href=\"https://en.wikipedia.org/wiki/Indian_people\">Indian</a>&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Music director\" href=\"https://en.wikipedia.org/wiki/Music_director\">music director</a>, composer,&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Musician\" href=\"https://en.wikipedia.org/wiki/Musician\">musician</a>&nbsp;and singer. His works are noted for integrating&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Indian classical music\" href=\"https://en.wikipedia.org/wiki/Indian_classical_music\">Indian classical music</a>&nbsp;with&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Electronic music\" href=\"https://en.wikipedia.org/wiki/Electronic_music\">electronic music</a>,&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"World music\" href=\"https://en.wikipedia.org/wiki/World_music\">world music</a>&nbsp;and traditional orchestral arrangements. Among his&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"List of awards and nominations received by A. R. Rahman\" href=\"https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_A._R._Rahman\">awards</a>&nbsp;are six&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"National Film Awards\" href=\"https://en.wikipedia.org/wiki/National_Film_Awards\">National Film Awards</a>, two&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Academy Awards\" href=\"https://en.wikipedia.org/wiki/Academy_Awards\">Academy Awards</a>, two&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Grammy Award\" href=\"https://en.wikipedia.org/wiki/Grammy_Award\">Grammy Awards</a>, a&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"British Academy Film Awards\" href=\"https://en.wikipedia.org/wiki/British_Academy_Film_Awards\">BAFTA Award</a>, a&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Golden Globe Award\" href=\"https://en.wikipedia.org/wiki/Golden_Globe_Award\">Golden Globe Award</a>, fifteen&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Filmfare Awards\" href=\"https://en.wikipedia.org/wiki/Filmfare_Awards\">Filmfare Awards</a>&nbsp;and seventeen&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Filmfare Awards South\" href=\"https://en.wikipedia.org/wiki/Filmfare_Awards_South\">Filmfare Awards South</a>. He has been awarded the&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Padma Bhushan\" href=\"https://en.wikipedia.org/wiki/Padma_Bhushan\">Padma Bhushan</a>, the third highest civilian award, in 2010 by the&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Government of India\" href=\"https://en.wikipedia.org/wiki/Government_of_India\">Government of India</a>.<sup id=\"cite_ref-1\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-1\">[1]</a></sup>&nbsp;In 2009, Rahman was included on the&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Time 100\" href=\"https://en.wikipedia.org/wiki/Time_100\"><em>Time</em>&nbsp;100 list of the world's most influential people</a>.<sup id=\"cite_ref-2\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-2\">[2]</a></sup>&nbsp;The UK-based world-music magazine&nbsp;<em><a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Songlines\" href=\"https://en.wikipedia.org/wiki/Songlines\">Songlines</a></em>&nbsp;named him one of \"Tomorrow's World Music Icons\" in August 2011.<sup id=\"cite_ref-3\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-3\">[3]</a></sup>&nbsp;He is nicknamed \"The Mozart of Madras\" and \"<em>Isai Puyal</em>\" (English:&nbsp;<span lang=\"en\">the Musical Storm</span>) in&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Tamil language\" href=\"https://en.wikipedia.org/wiki/Tamil_language\">Tamil</a>.<sup id=\"cite_ref-4\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-4\">[4]</a></sup></p>\r\n<p style=\"margin: 0.5em 0px; line-height: inherit; color: #222222; font-family: sans-serif;\">With an in-house studio (<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Panchathan Record Inn and AM Studios\" href=\"https://en.wikipedia.org/wiki/Panchathan_Record_Inn_and_AM_Studios\">Panchathan Record Inn</a>&nbsp;in&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Chennai\" href=\"https://en.wikipedia.org/wiki/Chennai\">Chennai</a>), Rahman's film-scoring career began during the early 1990s with the Tamil film&nbsp;<em><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Roja\" href=\"https://en.wikipedia.org/wiki/Roja\">Roja</a></em>. Working in&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Cinema of India\" href=\"https://en.wikipedia.org/wiki/Cinema_of_India\">India's film industries</a>,&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"World cinema\" href=\"https://en.wikipedia.org/wiki/World_cinema\">international cinema</a>, and theatre, Rahman is one of the best-selling recording artists,<sup id=\"cite_ref-5\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-5\">[5]</a></sup><sup id=\"cite_ref-6\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-6\">[6]</a></sup><sup id=\"cite_ref-Richard_Corliss_7-0\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-Richard_Corliss-7\">[7]</a></sup>&nbsp;with an estimated 200<span class=\"nowrap\" style=\"white-space: nowrap;\">&nbsp;</span>million units sold worldwide.<sup id=\"cite_ref-release_8-0\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-release-8\">[8]</a></sup>&nbsp;Rahman has also become a notable humanitarian and philanthropist, donating and raising money for a number of causes and charities. In 2017, Rahman made his debut as a director and writer for the film&nbsp;<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Le Musk (film)\" href=\"https://en.wikipedia.org/wiki/Le_Musk_(film)\"><em>Le Musk</em></a>.<sup id=\"cite_ref-9\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-9\">[9]</a></sup></p>",
            "city": 1
        }
    ]
}


##5 Event Details
http://13.234.60.82/api/event/shreya-ghoshal-live-in-concert/?domain=in

Response

    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "title": "Shreya Ghoshal Live in Concert",
                "slug": "shreya-ghoshal-live-in-concert",
                "ticket_type": "Multiple Ticket",
                "description": "<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">The most talented and versatile playback singer with multi-language singing skills. Won four National Film Awards, Six Filmfare Awards including Five for the Best Female Playback Singer, Nine Filmfare Awards South, Four Kerala State Film Awards and two Tamil Nadu State Film Awards. Shreya shot into fame, at the age of sixteen, when she won the television singing reality show Sa Re Ga Ma Pa. She has sung more than 80 odd songs in Malayalam movies and all her songs are superhits. Shreya Ghoshal is going to perform for the first time in Kozhikode.</p>\r\n<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">&nbsp;</p>\r\n<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">Why Kozhikode?</p>\r\n<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">Absolute ardent music lovers. Relish all genres of music with equal awe. Lovingly called the &ldquo;City of Music.&rdquo;Thus, Kozhikode will be the ideal venue to host &ldquo;Shreya Ghoshal&rdquo; for the first time. Expecting a huge crowd of music lovers, especially the fans of Shreya Ghoshal from the nearby districts like Malappuram, Wayanad, Kannur, and Kasargod as well.</p>",
                "host_details": "",
                "itinerary": "",
                "cancellation_policy": "<ul style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px 15px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; list-style-position: initial; list-style-image: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">Age Limit: 3+</li>\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">Internet handling fee per ticket may be levied. Please check your total amount before payment.</li>\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">Tickets once booked cannot be exchanged or refunded.</li>\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">We recommend that you arrive at least 20 minutes prior at the venue to pick up your physical tickets.</li>\r\n</ul>",
                "start_time": "2019-05-10T17:30:41.000000Z",
                "end_time": "2019-05-11T22:30:56.000000Z",
                "city": {
                    "name": "Kochi",
                    "short_name": "KOK",
                    "slug": "kochi-kerala"
                },
                "booking": {
                    "type": "Bookable",
                    "button_text": "Book Now",
                    "external_url": "None"
                },
                "category": {
                    "category_id": 1,
                    "name": "Music Show",
                    "slug": "music-show",
                    "weight": 1
                },
                "gallery": [
                    {
                        "id": 1,
                        "category_type": "IMG",
                        "category_name": "cate",
                        "upload": "http://13.234.60.82/media/Catagory_cate/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                    }
                ],
                "get_original": "/media/Events/1556192147/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29.jpg",
                "medias": {
                    "thumbnail": "http://13.234.60.82/media/Events/1556192147/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29_100x100.jpg",
                    "medium": "http://13.234.60.82/media/Events/1556192147/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29_300x300.jpg",
                    "large": "http://13.234.60.82/media/Events/1556192147/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29.jpg"
                },
                "slots": [
                    {
                        "start_time": "2019-05-10T17:30:41.000000Z",
                        "end_time": "2019-05-10T22:30:56.000000Z",
                        "max_size": 1000,
                        "slotpc_set": [
                            {
                                "seating_id": "747e27d7-bb4f-40af-8cb7-fecc053c0c1b",
                                "price_cat": {
                                    "id": 1,
                                    "title": "Entry Pass 1",
                                    "description": "Vip entry",
                                    "price": 1750,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 1
                            },
                            {
                                "seating_id": "fb9b5dfc-4ed1-484c-9ee3-17fae8ddc1e4",
                                "price_cat": {
                                    "id": 2,
                                    "title": "Entry Pass 2",
                                    "description": "Free drinks",
                                    "price": 1250,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 1
                            },
                            {
                                "seating_id": "f48465c4-b239-4210-ba76-80aea346da31",
                                "price_cat": {
                                    "id": 3,
                                    "title": "Entry Pass 3",
                                    "description": "",
                                    "price": 600,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 1
                            },
                            {
                                "seating_id": "7cf44bfb-61a3-440f-916c-075f23f553a8",
                                "price_cat": {
                                    "id": 4,
                                    "title": "Entry Pass 4",
                                    "description": "",
                                    "price": 350,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 1
                            }
                        ]
                    },
                    {
                        "start_time": "2019-05-11T17:30:41.000000Z",
                        "end_time": "2019-05-11T22:30:56.000000Z",
                        "max_size": 1000,
                        "slotpc_set": [
                            {
                                "seating_id": "af811aeb-54d6-4e3a-9342-ba6e420fdd53",
                                "price_cat": {
                                    "id": 1,
                                    "title": "Entry Pass 1",
                                    "description": "Vip entry",
                                    "price": 1750,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 2
                            },
                            {
                                "seating_id": "7cd019bc-8902-4fea-9ff2-7a3335cc8ffc",
                                "price_cat": {
                                    "id": 2,
                                    "title": "Entry Pass 2",
                                    "description": "Free drinks",
                                    "price": 1250,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 2
                            },
                            {
                                "seating_id": "bcfa374a-8c38-46ec-8265-c57848a653d2",
                                "price_cat": {
                                    "id": 3,
                                    "title": "Entry Pass 3",
                                    "description": "",
                                    "price": 600,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 2
                            },
                            {
                                "seating_id": "80fed4d8-13a5-47af-8a1c-a8f00065b879",
                                "price_cat": {
                                    "id": 4,
                                    "title": "Entry Pass 4",
                                    "description": "",
                                    "price": 350,
                                    "false_price": 0,
                                    "max_size": 100,
                                    "additional_charge": 0,
                                    "additional_charge_label": null
                                },
                                "booked_seats": 0,
                                "remaining_seats": 100,
                                "limitCategory": 100,
                                "limitSlot": 1000,
                                "totalSlot": 1000,
                                "event": 1,
                                "slot": 2
                            }
                        ]
                    }
                ],
                "address_venue": {
                    "title": "Crowne Plaza Kochi",
                    "label": "",
                    "capacity": 150,
                    "rate": 123,
                    "about": "<p><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span></p>",
                    "type": {
                        "id": 1,
                        "title": "Resort"
                    },
                    "upload": [
                        {
                            "id": 1,
                            "image_name": "image1",
                            "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                        }
                    ],
                    "location": {
                        "place": "Crowne Plaza Kochi, Kundannoor, Junction, Kochi, Kerala, India",
                        "latitude": 9.9341165,
                        "longitude": 76.31893739999998
                    }
                },
                "artists": [
                    {
                        "id": 2,
                        "artistImage": [
                            {
                                "id": 2,
                                "image_name": "shreya1",
                                "upload": "http://13.234.60.82/media/ArtistPhotos/shreya1/p05f6tb3.jpg"
                            },
                            {
                                "id": 3,
                                "image_name": "shreya2",
                                "upload": "http://13.234.60.82/media/ArtistPhotos/shreya2/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                            }
                        ],
                        "artistSong": [],
                        "title": "Shreya Ghoshal",
                        "thumbnail": null,
                        "slug": "shreya-ghoshal",
                        "fb_followers": 2500,
                        "inst_followers": null,
                        "rate": null,
                        "about": "<p><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">Playback singer Shreya Ghoshal started her illustrious career in 2002 after she was noticed by Sanjay Leela Bhansali when she won the musical reality show Sa Re Ga Ma Pa at the age of sixteen and subsequently sang five songs in his film, Devdas. Her seductive numbers in Jism established her as a versatile singer in the industry, and since then she has only seen progress in her career. Working with big names in the industry, like Anu Malik, Shankar-Ehsaan-Loy, Nadeem-Shravan she lent her voice to popular songs like Piyu Bole, Dheere Jalna, Agar Tum Mil Jao, Pehle Se, Hum To Aise Hain, Yeh Ishq Haaye, Mere Dholna, Main Agar Kahoon, Deewani Mastani, Pinga among many more, before she was associated with Bucket List (2018). Her other 2018 releases include Padmaavat, Sanju and Dhadak.&nbsp;</span><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">A recipient of four National Film Awards and six Filmfare Awards, Shreya became the first Indian singer to get a wax statue in the Indian Madame Tussauds. Apart from Hindi cinema, she is widely known for her songs in the South Indian film industry as well, like Yen Chellam in Album (2002), Munbe Vaa composed by A. R. Rahman, for which she bagged the Tamil Nadu State Film Award. She has also appeared in several musical reality TV shows. Ted Strickland, the governor of Ohio declared 26 June as 'Shreya Ghoshal Day'. She was awarded the highest honour in London by the members of House of Commons of the United Kingdom on April 2013.</span></p>",
                        "city": 1
                    }
                ]
            }
        ]
    }



##6 Order API 
http://13.234.60.82/api/order/

Request

    {
     
     "event":14,
     "slot":14,
     
     "cust_name":"naseem2",
     "cust_email":"naseem.10@gmail.com",
     "cust_phone":"9947267251",
     
     "is_order_seller":false,
     
     
    
     "grandtotal":13360.00,
      "io_id": [{"item_id":11,"item_name":"Gate C Entry","item_price":1180.0,"count":2,"pc_cat":11,"pc_slot":"7ffc9bd8-2d6c-4bb9-9e32-072b196b6fab","additional_charge":0},
      {"item_id":14,"item_name":"Gate A entry","item_price":5500.0,"count":2,"pc_cat":14,"pc_slot":"8cad1b4e-66f8-4764-a9ed-880c97ea0e6c","additional_charge":0}],
      "order_no":1123343ASDDFD
    }


#Response
    {
        "razororder": {
            "id": "order_CHvdtcBRB1SsdC",
            "entity": "order",
            "amount": 1336000,
            "amount_paid": 0,
            "amount_due": 1336000,
            "currency": "INR",
            "receipt": "rcptIdTsjLjiesCJys4MXgNw4DrK",
            "offer_id": null,
            "status": "created",
            "attempts": 0,
            "notes": {
                "key": "value"
            },
            "created_at": 1554894218
        },
        "order_details": {
            "event": 14,
            "slot": 14,
            "cust_name": "naseem2",
            "cust_email": "naseem.10@gmail.com",
            "cust_phone": "9947267251",
            "ordercreatedtime": "2019-04-10T16:33:37.824375Z",
            "grandtotal": 1336000,
            "io_id": [
                {
                    "item_name": "Gate C Entry",
                    "pc_cat": 11,
                    "pc_slot": "7ffc9bd8-2d6c-4bb9-9e32-072b196b6fab",
                    "count": 2,
                    "item_price": 1180,
                    "additional_charge": 0
                },
                {
                    "item_name": "Gate A entry",
                    "pc_cat": 14,
                    "pc_slot": "8cad1b4e-66f8-4764-a9ed-880c97ea0e6c",
                    "count": 2,
                    "item_price": 5500,
                    "additional_charge": 0
                }
            ],
            "order_no": "rcptIdTsjLjiesCJys4MXgNw4DrK",
            "payment_status": "Payment Pending",
            "order_status": "Order Completed",
            "id": "e4c6cb0f-e45f-4006-afc7-3e3ab22c5748",
            "ticket_code": "B25F51",
            "seller": null,
            "is_order_seller": false
        },
        "status": true
    }
    
##7 Payment
http://13.234.60.82/api/payment-fetch/

Request
{"razorpay_order_id":"order_CHvdtcBRB1SsdC","razorpay_payment_id":"pay_CHvgSxZtW0sKev",
"razorpay_signature":"040041cbc4ef388d78c6b5dc33c093a2b16487b7352693a24af27ca76e07ec7d"
}


Response
{
    "cont": "{'orderdetails': {'cust_name': 'naseem2', 'cust_email': 'naseem.10@gmail.com', 'event': <Event: AR Rahman Show>, 'slot': <Slot: None:2019-01-28 06:36:10+00:00  :14 >, 'cust_phone': '9947267251', 'grandtotal': 13360.0, 'order_no': UUID('e4c6cb0f-e45f-4006-afc7-3e3ab22c5748')}, 'itemdetails': [{'item_name': 'Gate C Entry', 'item_price': 1180.0, 'count': 2}, {'item_name': 'Gate A entry', 'item_price': 5500.0, 'count': 2}], 'context': {'video_id': 'J9go2nj6b3M', 'options_example': <qr_code.qrcode.utils.QRCodeOptions object at 0x112aa5e80>}}",
    "success": "Payment Completed succesfully",
    "notify sms": {
        "sms": "message sent succsfully"
    }
}


##8 Artist Details
http://13.234.60.82/api/artist/shreya-ghoshal/

Response
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "artistImage": [
                {
                    "id": 2,
                    "image_name": "shreya1",
                    "upload": "http://13.234.60.82/media/ArtistPhotos/shreya1/p05f6tb3.jpg"
                },
                {
                    "id": 3,
                    "image_name": "shreya2",
                    "upload": "http://13.234.60.82/media/ArtistPhotos/shreya2/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                }
            ],
            "artistSong": [],
            "title": "Shreya Ghoshal",
            "thumbnail": null,
            "slug": "shreya-ghoshal",
            "fb_followers": 2500,
            "inst_followers": null,
            "rate": null,
            "about": "<p><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">Playback singer Shreya Ghoshal started her illustrious career in 2002 after she was noticed by Sanjay Leela Bhansali when she won the musical reality show Sa Re Ga Ma Pa at the age of sixteen and subsequently sang five songs in his film, Devdas. Her seductive numbers in Jism established her as a versatile singer in the industry, and since then she has only seen progress in her career. Working with big names in the industry, like Anu Malik, Shankar-Ehsaan-Loy, Nadeem-Shravan she lent her voice to popular songs like Piyu Bole, Dheere Jalna, Agar Tum Mil Jao, Pehle Se, Hum To Aise Hain, Yeh Ishq Haaye, Mere Dholna, Main Agar Kahoon, Deewani Mastani, Pinga among many more, before she was associated with Bucket List (2018). Her other 2018 releases include Padmaavat, Sanju and Dhadak.&nbsp;</span><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">A recipient of four National Film Awards and six Filmfare Awards, Shreya became the first Indian singer to get a wax statue in the Indian Madame Tussauds. Apart from Hindi cinema, she is widely known for her songs in the South Indian film industry as well, like Yen Chellam in Album (2002), Munbe Vaa composed by A. R. Rahman, for which she bagged the Tamil Nadu State Film Award. She has also appeared in several musical reality TV shows. Ted Strickland, the governor of Ohio declared 26 June as 'Shreya Ghoshal Day'. She was awarded the highest honour in London by the members of House of Commons of the United Kingdom on April 2013.</span></p>",
            "city": 1
        }
    ]
}

##9 Venue Details
http://13.234.60.82/api/venue/crowne-plaza-kochi/

Response
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Crowne Plaza Kochi",
            "label": "",
            "capacity": 150,
            "rate": 123,
            "about": "<p><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span></p>",
            "type": {
                "id": 1,
                "title": "Resort"
            },
            "upload": [
                {
                    "id": 1,
                    "image_name": "image1",
                    "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                }
            ],
            "location": {
                "place": "Crowne Plaza Kochi, Kundannoor, Junction, Kochi, Kerala, India",
                "latitude": 9.9341165,
                "longitude": 76.31893739999998
            }
        }
    ]
}

##10 Home API

http://13.234.60.82/api/home/



{
    "status": 200,
    "banner": [
        {
            "image": "http://13.234.60.82/media/collabo_banner/ar_rahman.jpeg",
            "title": "Tiyan",
            "event": 2
        },
        {
            "image": "http://13.234.60.82/media/collabo_banner/collabo.jpg",
            "title": "Athul Live",
            "event": 7
        }
    ],
    "featureartist": [
        {
            "name": "Artists in kochi",
            "slug": "artists-in-kochi",
            "id": 1,
            "city": 1,
            "artist": [
                {
                    "id": 1,
                    "artistImage": [
                        {
                            "id": 1,
                            "image_name": "ar rahman",
                            "upload": "http://13.234.60.82/media/ArtistPhotos/ar%20rahman/ar_rahman.jpeg"
                        }
                    ],
                    "artistSong": [
                        {
                            "id": 1,
                            "image_name": "A. R. Rahman Meets Berklee - V",
                            "upload": "https://www.youtube.com/watch?v=Ss-kLGW2pHQ",
                            "links": "YT"
                        }
                    ],
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    },
                    "title": "AR Rahman",
                    "thumbnail": null,
                    "slug": "ar-rahman",
                    "fb_followers": 1234,
                    "inst_followers": 1235,
                    "rate": 124,
                    "about": "<p style=\"margin: 0.5em 0px; line-height: inherit; color: #222222; font-family: sans-serif;\"><strong>Allahrakka Rahman</strong>&nbsp;(<span class=\"unicode haudio\"><span class=\"fn\"><span style=\"white-space: nowrap; margin-right: 0.25em;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"About this sound\" href=\"https://en.wikipedia.org/wiki/File:A_R_Rahman.ogg\"><img style=\"border: 0px; vertical-align: middle; margin: 0px;\" src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x\" alt=\"About this sound\" width=\"11\" height=\"11\" data-file-width=\"20\" data-file-height=\"20\" /></a></span><a class=\"internal\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"A R Rahman.ogg\" href=\"https://upload.wikimedia.org/wikipedia/commons/9/9c/A_R_Rahman.ogg\">pronunciation</a></span>&nbsp;<small class=\"metadata audiolinkinfo\" style=\"font-size: 11.9px; cursor: help;\">(<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Wikipedia:Media help\" href=\"https://en.wikipedia.org/wiki/Wikipedia:Media_help\"><span style=\"cursor: help;\">help</span></a>&middot;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"File:A R Rahman.ogg\" href=\"https://en.wikipedia.org/wiki/File:A_R_Rahman.ogg\"><span style=\"cursor: help;\">info</span></a>)</small></span>; born&nbsp;<strong>A. S. Dileep Kumar</strong>) known professionally as&nbsp;<strong>A. R. Rahman</strong>, is an&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Indian people\" href=\"https://en.wikipedia.org/wiki/Indian_people\">Indian</a>&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Music director\" href=\"https://en.wikipedia.org/wiki/Music_director\">music director</a>, composer,&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Musician\" href=\"https://en.wikipedia.org/wiki/Musician\">musician</a>&nbsp;and singer. His works are noted for integrating&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Indian classical music\" href=\"https://en.wikipedia.org/wiki/Indian_classical_music\">Indian classical music</a>&nbsp;with&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Electronic music\" href=\"https://en.wikipedia.org/wiki/Electronic_music\">electronic music</a>,&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"World music\" href=\"https://en.wikipedia.org/wiki/World_music\">world music</a>&nbsp;and traditional orchestral arrangements. Among his&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"List of awards and nominations received by A. R. Rahman\" href=\"https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_A._R._Rahman\">awards</a>&nbsp;are six&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"National Film Awards\" href=\"https://en.wikipedia.org/wiki/National_Film_Awards\">National Film Awards</a>, two&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Academy Awards\" href=\"https://en.wikipedia.org/wiki/Academy_Awards\">Academy Awards</a>, two&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Grammy Award\" href=\"https://en.wikipedia.org/wiki/Grammy_Award\">Grammy Awards</a>, a&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"British Academy Film Awards\" href=\"https://en.wikipedia.org/wiki/British_Academy_Film_Awards\">BAFTA Award</a>, a&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Golden Globe Award\" href=\"https://en.wikipedia.org/wiki/Golden_Globe_Award\">Golden Globe Award</a>, fifteen&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Filmfare Awards\" href=\"https://en.wikipedia.org/wiki/Filmfare_Awards\">Filmfare Awards</a>&nbsp;and seventeen&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Filmfare Awards South\" href=\"https://en.wikipedia.org/wiki/Filmfare_Awards_South\">Filmfare Awards South</a>. He has been awarded the&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Padma Bhushan\" href=\"https://en.wikipedia.org/wiki/Padma_Bhushan\">Padma Bhushan</a>, the third highest civilian award, in 2010 by the&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Government of India\" href=\"https://en.wikipedia.org/wiki/Government_of_India\">Government of India</a>.<sup id=\"cite_ref-1\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-1\">[1]</a></sup>&nbsp;In 2009, Rahman was included on the&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Time 100\" href=\"https://en.wikipedia.org/wiki/Time_100\"><em>Time</em>&nbsp;100 list of the world's most influential people</a>.<sup id=\"cite_ref-2\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-2\">[2]</a></sup>&nbsp;The UK-based world-music magazine&nbsp;<em><a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Songlines\" href=\"https://en.wikipedia.org/wiki/Songlines\">Songlines</a></em>&nbsp;named him one of \"Tomorrow's World Music Icons\" in August 2011.<sup id=\"cite_ref-3\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-3\">[3]</a></sup>&nbsp;He is nicknamed \"The Mozart of Madras\" and \"<em>Isai Puyal</em>\" (English:&nbsp;<span lang=\"en\">the Musical Storm</span>) in&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Tamil language\" href=\"https://en.wikipedia.org/wiki/Tamil_language\">Tamil</a>.<sup id=\"cite_ref-4\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-4\">[4]</a></sup></p>\r\n<p style=\"margin: 0.5em 0px; line-height: inherit; color: #222222; font-family: sans-serif;\">With an in-house studio (<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Panchathan Record Inn and AM Studios\" href=\"https://en.wikipedia.org/wiki/Panchathan_Record_Inn_and_AM_Studios\">Panchathan Record Inn</a>&nbsp;in&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Chennai\" href=\"https://en.wikipedia.org/wiki/Chennai\">Chennai</a>), Rahman's film-scoring career began during the early 1990s with the Tamil film&nbsp;<em><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Roja\" href=\"https://en.wikipedia.org/wiki/Roja\">Roja</a></em>. Working in&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Cinema of India\" href=\"https://en.wikipedia.org/wiki/Cinema_of_India\">India's film industries</a>,&nbsp;<a style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"World cinema\" href=\"https://en.wikipedia.org/wiki/World_cinema\">international cinema</a>, and theatre, Rahman is one of the best-selling recording artists,<sup id=\"cite_ref-5\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-5\">[5]</a></sup><sup id=\"cite_ref-6\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-6\">[6]</a></sup><sup id=\"cite_ref-Richard_Corliss_7-0\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-Richard_Corliss-7\">[7]</a></sup>&nbsp;with an estimated 200<span class=\"nowrap\" style=\"white-space: nowrap;\">&nbsp;</span>million units sold worldwide.<sup id=\"cite_ref-release_8-0\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-release-8\">[8]</a></sup>&nbsp;Rahman has also become a notable humanitarian and philanthropist, donating and raising money for a number of causes and charities. In 2017, Rahman made his debut as a director and writer for the film&nbsp;<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0b0080; background: none;\" title=\"Le Musk (film)\" href=\"https://en.wikipedia.org/wiki/Le_Musk_(film)\"><em>Le Musk</em></a>.<sup id=\"cite_ref-9\" class=\"reference\" style=\"line-height: 1; unicode-bidi: isolate; white-space: nowrap; font-size: 11.2px;\"><a style=\"text-decoration-line: none; color: #0b0080; background: none;\" href=\"https://en.wikipedia.org/wiki/A._R._Rahman#cite_note-9\">[9]</a></sup></p>"
                },
                {
                    "id": 2,
                    "artistImage": [
                        {
                            "id": 2,
                            "image_name": "shreya1",
                            "upload": "http://13.234.60.82/media/ArtistPhotos/shreya1/p05f6tb3.jpg"
                        },
                        {
                            "id": 3,
                            "image_name": "shreya2",
                            "upload": "http://13.234.60.82/media/ArtistPhotos/shreya2/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                        }
                    ],
                    "artistSong": [],
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    },
                    "title": "Shreya Ghoshal",
                    "thumbnail": null,
                    "slug": "shreya-ghoshal",
                    "fb_followers": 2500,
                    "inst_followers": null,
                    "rate": null,
                    "about": "<p><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">Playback singer Shreya Ghoshal started her illustrious career in 2002 after she was noticed by Sanjay Leela Bhansali when she won the musical reality show Sa Re Ga Ma Pa at the age of sixteen and subsequently sang five songs in his film, Devdas. Her seductive numbers in Jism established her as a versatile singer in the industry, and since then she has only seen progress in her career. Working with big names in the industry, like Anu Malik, Shankar-Ehsaan-Loy, Nadeem-Shravan she lent her voice to popular songs like Piyu Bole, Dheere Jalna, Agar Tum Mil Jao, Pehle Se, Hum To Aise Hain, Yeh Ishq Haaye, Mere Dholna, Main Agar Kahoon, Deewani Mastani, Pinga among many more, before she was associated with Bucket List (2018). Her other 2018 releases include Padmaavat, Sanju and Dhadak.&nbsp;</span><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">A recipient of four National Film Awards and six Filmfare Awards, Shreya became the first Indian singer to get a wax statue in the Indian Madame Tussauds. Apart from Hindi cinema, she is widely known for her songs in the South Indian film industry as well, like Yen Chellam in Album (2002), Munbe Vaa composed by A. R. Rahman, for which she bagged the Tamil Nadu State Film Award. She has also appeared in several musical reality TV shows. Ted Strickland, the governor of Ohio declared 26 June as 'Shreya Ghoshal Day'. She was awarded the highest honour in London by the members of House of Commons of the United Kingdom on April 2013.</span></p>"
                },
                {
                    "id": 4,
                    "artistImage": [],
                    "artistSong": [],
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    },
                    "title": "Atul Khatri",
                    "thumbnail": "http://13.234.60.82/media/Artist/Atul%20Khatri/atul.jpg",
                    "slug": "atul-khatri",
                    "fb_followers": 297000,
                    "inst_followers": 127500,
                    "rate": null,
                    "about": "<div class=\"event-details\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\">\r\n<div class=\"container\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: auto; padding: 24px; -webkit-box-flex: 1; flex: 1 1 100%; width: 1185px; max-width: 1185px;\">\r\n<div class=\"layout column wrap\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; display: flex; -webkit-box-flex: 1; flex: 1 1 auto; flex-flow: column wrap; min-width: 0px; -webkit-box-orient: vertical; -webkit-box-direction: normal;\">\r\n<div class=\"flex mt-4\" style=\"box-sizing: inherit; background-repeat: no-repeat; padding: 0px; -webkit-box-flex: 1; flex: 1 1 auto; max-width: 100%; margin: 24px !important 0px 0px 0px;\">\r\n<div style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px;\">\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px;\"><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">Can businessmen be funny? Yes. Meet Atul Khatri, a middle-aged businessman- turned-comedian who now makes a living making people laugh harder than they ever have. A past member of one of the country's leading comedy collectives, East India Comedy, Atul has appeared on their YouTube series like EIC Outrage, and specials such as EIC vs Bollywood. Bringing his 40+- year-old perspective with every show, he performs regularly at comedy clubs and does private shows in India and abroad. The comedian has showcased his skills at the prestigious Utrecht International Comedy Festival in the Netherlands and Belgium and at the 8th Annual Hong Kong International Comedy Festival in 2014. CNN-IBN recently rated him as one of the Top 20 Comedians in India to Watch Out For, post winning the competition CEOs Got Talent.</span></p>\r\n</div>\r\n</div>\r\n</div>\r\n</div>\r\n</div>\r\n<div class=\"host-details\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\">\r\n<div class=\"container\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: auto; padding: 24px; -webkit-box-flex: 1; flex: 1 1 100%; width: 1185px; max-width: 1185px;\">&nbsp;</div>\r\n</div>"
                }
            ]
        }
    ],
    "featureevent": [
        {
            "name": "Events in Kochi",
            "slug": "events-in-kochi",
            "id": 1,
            "city": 1,
            "event": [
                {
                    "id": 8,
                    "title": "Kochi Tech Summit",
                    "short_title": null,
                    "slug": "kochi-tech-summit",
                    "ticket_type": "Single Ticket",
                    "description": "<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\"><span style=\"font-family: helvetica, arial, sans-serif; font-size: 10pt;\">Welcome to the Kochi Tech Summit - 2019!</span></p>\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\"><span style=\"font-family: helvetica, arial, sans-serif; font-size: 10pt;\">The Tech Summit provides a unique opportunity to connect with fellow digital enthusiasts working new technologies, domain &amp; fields. By bringing people together ranging from the MNCs, Industries, start-ups, regulators, education institutes, the biggest Corporate.</span></p>\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\"><span style=\"font-family: helvetica, arial, sans-serif; font-size: 10pt;\">Exploring a myriad of themes and topics such as Emerging Technologies like Blockchain, IoT, AI &amp; ML, Smart City and the Mobility, Industry 4.0, Agri Tech and much more.​</span></p>\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\"><span style=\"font-family: helvetica, arial, sans-serif; font-size: 10pt;\">This Summit will be an ideal platform for the people from any industries, technologies to understand and to leverage the latest technical use cases, work &amp; innovations on our businesses and daily lives.</span></p>\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\"><span style=\"font-family: helvetica, arial, sans-serif; font-size: 10pt;\">This helps its participants/delegates to understand how the new technologies work from the view of the business/start-ups.</span></p>\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\"><span style=\"font-family: helvetica, arial, sans-serif; font-size: 10pt;\">Tech Summit will bring Founder &amp; Co-Founders, Investors, Innovators, Developers, Students and C-Level decision makers at the same place.</span></p>",
                    "host_details": "",
                    "itinerary": "",
                    "cancellation_policy": "",
                    "start_time": "2019-06-15T09:30:00.000000Z",
                    "end_time": "2019-06-15T17:30:00.000000Z",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    },
                    "booking": {
                        "type": "Bookable",
                        "button_text": "Register Now",
                        "external_url": "None"
                    },
                    "category": {
                        "category_id": 3,
                        "name": "Business",
                        "slug": "business",
                        "weight": 0
                    },
                    "gallery": [
                        {
                            "id": 7,
                            "category_type": "IMG",
                            "category_name": "Kochi Tech Summit",
                            "upload": "http://13.234.60.82/media/Catagory_Kochi%20Tech%20Summit/Sadie_and_Wesley_3.png"
                        }
                    ],
                    "get_original": "/media/Events/1557828307/Sadie_and_Wesley_3.png",
                    "medias": {
                        "thumbnail": "http://13.234.60.82/media/Events/1557828307/Sadie_and_Wesley_3_100x100.jpg",
                        "medium": "http://13.234.60.82/media/Events/1557828307/Sadie_and_Wesley_3_300x300.jpg",
                        "large": "http://13.234.60.82/media/Events/1557828307/Sadie_and_Wesley_3.png"
                    },
                    "slots": [
                        {
                            "start_time": "2019-06-15T09:30:00.000000Z",
                            "end_time": "2019-06-15T17:30:00.000000Z",
                            "max_size": 500,
                            "slotpc_set": [
                                {
                                    "seating_id": "0e65fc27-e698-484a-92d4-673812fab885",
                                    "price_cat": {
                                        "id": 11,
                                        "title": "Early Bird Entry",
                                        "description": "Inclusive of 18% GST. Registration Ends on 01 June 2019",
                                        "price": 1770,
                                        "false_price": 0,
                                        "max_size": null,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 500,
                                    "limitCategory": null,
                                    "limitSlot": 500,
                                    "totalSlot": 500,
                                    "event": 8,
                                    "slot": 8
                                }
                            ]
                        }
                    ],
                    "address_venue": {
                        "title": "The Grant Conference Hall",
                        "label": "The Classik Fort",
                        "capacity": 500,
                        "rate": null,
                        "about": "<p><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">The Classik Fort Hotel offers five convention spaces for various purposes including both formal and informal events. The Ceremony Convention Hall has a 3200 square feet can accommodate 500 people in the classroom and 1000 people in floating crowd style.</span></p>\r\n<p><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">The Grant Conference Hall (2100 square feet), Regent Banquet Hall (1400 square feet) and Senate Hall (1200 square feet) can accommodate 350, 250 and 150 people in the classroom style and 500, 300 and 200 people in the floating crowd consecutively. For your audio/visual needs, the hotel is also equipped with the latest technology including projector, wireless hand-held microphones.&nbsp;</span></p>",
                        "type": {
                            "id": 3,
                            "title": "Indoor Hall"
                        },
                        "upload": [
                            {
                                "id": 6,
                                "image_name": "Classic Fort",
                                "upload": "http://13.234.60.82/media/VenuePhotos/Classic%20Fort/The-Classik-Fort-IMG-20151023-WA0011.jpg"
                            }
                        ],
                        "location": {
                            "place": "The Classik Fort, Thripunithura - Maradu Road, Gandhi Square, Poonithura, Maradu, Kochi, Kerala, India",
                            "latitude": 9.943833,
                            "longitude": 76.33528100000001
                        },
                        "slug": "the-grant-conference-hall",
                        "city": {
                            "name": "Kochi",
                            "short_name": "KOK",
                            "slug": "kochi",
                            "payment_method": "PAYTM"
                        }
                    },
                    "artists": [],
                    "lowest_price": 1770
                },
                {
                    "id": 1,
                    "title": "Shreya Ghoshal Live in Concert",
                    "short_title": null,
                    "slug": "shreya-ghoshal-live-in-concert",
                    "ticket_type": "Multiple Ticket",
                    "description": "<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">The most talented and versatile playback singer with multi-language singing skills. Won four National Film Awards, Six Filmfare Awards including Five for the Best Female Playback Singer, Nine Filmfare Awards South, Four Kerala State Film Awards and two Tamil Nadu State Film Awards. Shreya shot into fame, at the age of sixteen, when she won the television singing reality show Sa Re Ga Ma Pa. She has sung more than 80 odd songs in Malayalam movies and all her songs are superhits. Shreya Ghoshal is going to perform for the first time in Kozhikode.</p>\r\n<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">&nbsp;</p>\r\n<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">Why Kozhikode?</p>\r\n<p style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">Absolute ardent music lovers. Relish all genres of music with equal awe. Lovingly called the &ldquo;City of Music.&rdquo;Thus, Kozhikode will be the ideal venue to host &ldquo;Shreya Ghoshal&rdquo; for the first time. Expecting a huge crowd of music lovers, especially the fans of Shreya Ghoshal from the nearby districts like Malappuram, Wayanad, Kannur, and Kasargod as well.</p>",
                    "host_details": "",
                    "itinerary": "",
                    "cancellation_policy": "<ul style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px 15px; padding: 0px; border: 0px; font-size: 12px; vertical-align: baseline; background-image: initial; background-position: 0px 0px; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; list-style-position: initial; list-style-image: initial; color: #999999; font-family: 'Roboto Regular', sans-serif;\">\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">Age Limit: 3+</li>\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">Internet handling fee per ticket may be levied. Please check your total amount before payment.</li>\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">Tickets once booked cannot be exchanged or refunded.</li>\r\n<li style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; border: 0px; vertical-align: baseline; background: 0px 0px;\">We recommend that you arrive at least 20 minutes prior at the venue to pick up your physical tickets.</li>\r\n</ul>",
                    "start_time": "2019-05-10T17:30:41.000000Z",
                    "end_time": "2019-05-11T22:30:56.000000Z",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    },
                    "booking": {
                        "type": "Bookable",
                        "button_text": "Book Now",
                        "external_url": "None"
                    },
                    "category": {
                        "category_id": 1,
                        "name": "Music Show",
                        "slug": "music-show",
                        "weight": 1
                    },
                    "gallery": [
                        {
                            "id": 1,
                            "category_type": "IMG",
                            "category_name": "cate",
                            "upload": "http://13.234.60.82/media/Catagory_cate/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                        }
                    ],
                    "get_original": "/media/Events/1557747425/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29.jpg",
                    "medias": {
                        "thumbnail": "http://13.234.60.82/media/Events/1557747425/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29_100x100.jpg",
                        "medium": "http://13.234.60.82/media/Events/1557747425/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29_300x300.jpg",
                        "large": "http://13.234.60.82/media/Events/1557747425/media-desktop-shreya-ghoshal-live-in-concert-2019-4-24-t-19-23-29.jpg"
                    },
                    "slots": [
                        {
                            "start_time": "2019-05-10T17:30:41.000000Z",
                            "end_time": "2019-05-10T22:30:56.000000Z",
                            "max_size": 1000,
                            "slotpc_set": [
                                {
                                    "seating_id": "747e27d7-bb4f-40af-8cb7-fecc053c0c1b",
                                    "price_cat": {
                                        "id": 1,
                                        "title": "Entry Pass 1",
                                        "description": "Vip entry",
                                        "price": 1750,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 1
                                },
                                {
                                    "seating_id": "fb9b5dfc-4ed1-484c-9ee3-17fae8ddc1e4",
                                    "price_cat": {
                                        "id": 2,
                                        "title": "Entry Pass 2",
                                        "description": "Free drinks",
                                        "price": 1250,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 1
                                },
                                {
                                    "seating_id": "f48465c4-b239-4210-ba76-80aea346da31",
                                    "price_cat": {
                                        "id": 3,
                                        "title": "Entry Pass 3",
                                        "description": "",
                                        "price": 600,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 1
                                },
                                {
                                    "seating_id": "7cf44bfb-61a3-440f-916c-075f23f553a8",
                                    "price_cat": {
                                        "id": 4,
                                        "title": "Entry Pass 4",
                                        "description": "",
                                        "price": 350,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 1
                                }
                            ]
                        },
                        {
                            "start_time": "2019-05-11T17:30:41.000000Z",
                            "end_time": "2019-05-11T22:30:56.000000Z",
                            "max_size": 1000,
                            "slotpc_set": [
                                {
                                    "seating_id": "af811aeb-54d6-4e3a-9342-ba6e420fdd53",
                                    "price_cat": {
                                        "id": 1,
                                        "title": "Entry Pass 1",
                                        "description": "Vip entry",
                                        "price": 1750,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 2
                                },
                                {
                                    "seating_id": "7cd019bc-8902-4fea-9ff2-7a3335cc8ffc",
                                    "price_cat": {
                                        "id": 2,
                                        "title": "Entry Pass 2",
                                        "description": "Free drinks",
                                        "price": 1250,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 2
                                },
                                {
                                    "seating_id": "bcfa374a-8c38-46ec-8265-c57848a653d2",
                                    "price_cat": {
                                        "id": 3,
                                        "title": "Entry Pass 3",
                                        "description": "",
                                        "price": 600,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 2
                                },
                                {
                                    "seating_id": "80fed4d8-13a5-47af-8a1c-a8f00065b879",
                                    "price_cat": {
                                        "id": 4,
                                        "title": "Entry Pass 4",
                                        "description": "",
                                        "price": 350,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 1,
                                    "slot": 2
                                }
                            ]
                        }
                    ],
                    "address_venue": {
                        "title": "Crowne Plaza Kochi",
                        "label": "",
                        "capacity": 150,
                        "rate": 123,
                        "about": "<p><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span></p>",
                        "type": {
                            "id": 1,
                            "title": "Resort"
                        },
                        "upload": [
                            {
                                "id": 1,
                                "image_name": "image1",
                                "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                            }
                        ],
                        "location": {
                            "place": "Crowne Plaza Kochi, Kundannoor, Junction, Kochi, Kerala, India",
                            "latitude": 9.9341165,
                            "longitude": 76.31893739999998
                        },
                        "slug": "crowne-plaza-kochi",
                        "city": {
                            "name": "Kochi",
                            "short_name": "KOK",
                            "slug": "kochi",
                            "payment_method": "PAYTM"
                        }
                    },
                    "artists": [
                        {
                            "id": 2,
                            "artistImage": [
                                {
                                    "id": 2,
                                    "image_name": "shreya1",
                                    "upload": "http://13.234.60.82/media/ArtistPhotos/shreya1/p05f6tb3.jpg"
                                },
                                {
                                    "id": 3,
                                    "image_name": "shreya2",
                                    "upload": "http://13.234.60.82/media/ArtistPhotos/shreya2/SHREYA-LIVE-IN-CONCERT-NEW-ZEE.jpg"
                                }
                            ],
                            "artistSong": [],
                            "city": {
                                "name": "Kochi",
                                "short_name": "KOK",
                                "slug": "kochi",
                                "payment_method": "PAYTM"
                            },
                            "title": "Shreya Ghoshal",
                            "thumbnail": null,
                            "slug": "shreya-ghoshal",
                            "fb_followers": 2500,
                            "inst_followers": null,
                            "rate": null,
                            "about": "<p><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">Playback singer Shreya Ghoshal started her illustrious career in 2002 after she was noticed by Sanjay Leela Bhansali when she won the musical reality show Sa Re Ga Ma Pa at the age of sixteen and subsequently sang five songs in his film, Devdas. Her seductive numbers in Jism established her as a versatile singer in the industry, and since then she has only seen progress in her career. Working with big names in the industry, like Anu Malik, Shankar-Ehsaan-Loy, Nadeem-Shravan she lent her voice to popular songs like Piyu Bole, Dheere Jalna, Agar Tum Mil Jao, Pehle Se, Hum To Aise Hain, Yeh Ishq Haaye, Mere Dholna, Main Agar Kahoon, Deewani Mastani, Pinga among many more, before she was associated with Bucket List (2018). Her other 2018 releases include Padmaavat, Sanju and Dhadak.&nbsp;</span><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><br style=\"-webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; outline: 0px; box-sizing: inherit; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\" /><span style=\"color: rgba(0, 0, 0, 0.54); font-family: Montserrat, sans-serif; text-align: justify;\">A recipient of four National Film Awards and six Filmfare Awards, Shreya became the first Indian singer to get a wax statue in the Indian Madame Tussauds. Apart from Hindi cinema, she is widely known for her songs in the South Indian film industry as well, like Yen Chellam in Album (2002), Munbe Vaa composed by A. R. Rahman, for which she bagged the Tamil Nadu State Film Award. She has also appeared in several musical reality TV shows. Ted Strickland, the governor of Ohio declared 26 June as 'Shreya Ghoshal Day'. She was awarded the highest honour in London by the members of House of Commons of the United Kingdom on April 2013.</span></p>"
                        }
                    ],
                    "lowest_price": 0
                },
                {
                    "id": 5,
                    "title": "ssd dfdg",
                    "short_title": "sadsf sds",
                    "slug": "ssd-dfdg",
                    "ticket_type": "Single Ticket",
                    "description": "",
                    "host_details": "",
                    "itinerary": "",
                    "cancellation_policy": "",
                    "start_time": null,
                    "end_time": null,
                    "city": {
                        "name": "Kottayam",
                        "short_name": "KTYM",
                        "slug": "kottayam",
                        "payment_method": "PAYTM"
                    },
                    "booking": {
                        "type": "Bookable",
                        "button_text": "None",
                        "external_url": "None"
                    },
                    "category": {
                        "category_id": 1,
                        "name": "Music Show",
                        "slug": "music-show",
                        "weight": 1
                    },
                    "gallery": [
                        {
                            "id": 5,
                            "category_type": "IMG",
                            "category_name": "Atul Khatri Kochi",
                            "upload": "http://13.234.60.82/media/Catagory_Atul%20Khatri%20Kochi/atul-khatri.jpg"
                        }
                    ],
                    "get_original": "/media/Events/1557825388/ahinoydonc-1532169510.jpg",
                    "medias": {
                        "thumbnail": "http://13.234.60.82/media/Events/1557828307/ahinoydonc-1532169510_100x100.jpg",
                        "medium": "http://13.234.60.82/media/Events/1557828307/ahinoydonc-1532169510_300x300.jpg",
                        "large": "http://13.234.60.82/media/Events/1557825388/ahinoydonc-1532169510.jpg"
                    },
                    "slots": [],
                    "address_venue": {
                        "title": "The Regent Hall",
                        "label": "MG Road, Kochi",
                        "capacity": 200,
                        "rate": null,
                        "about": "<p style=\"margin: 0px 0px 16px; padding: 0px; border: 0px; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-stretch: inherit; font-size: 13.008px; line-height: 1.5em; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; outline: 0px; color: #7b7168;\"><span style=\"color: #000000;\">The Avenue Regent is located in the heart of the city with 60 luxury rooms, a tapas bar and houses one of the best cafes in town. The recently renovated Regent Hall is spacious and grand with high ceilings and silk wall-panellings. This pillar-less hall is ideal for wedding receptions and large conferences accommodating up to 200 seats in a theatre-style arrangement.</span></p>\r\n<p><strong><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">Valet parking available</span></strong></p>",
                        "type": {
                            "id": 3,
                            "title": "Indoor Hall"
                        },
                        "upload": [
                            {
                                "id": 5,
                                "image_name": "Regent Hall",
                                "upload": "http://13.234.60.82/media/VenuePhotos/Regent%20Hall/regent_hall.jpg"
                            }
                        ],
                        "location": {
                            "place": "The Avenue Regent, Mahatma Gandhi Road, Jos Junction, Pallimukku, Kochi, Kerala, India",
                            "latitude": 9.966751,
                            "longitude": 76.28666199999998
                        },
                        "slug": "the-regent-hall",
                        "city": {
                            "name": "Kochi",
                            "short_name": "KOK",
                            "slug": "kochi",
                            "payment_method": "PAYTM"
                        }
                    },
                    "artists": [],
                    "lowest_price": 0
                },
                {
                    "id": 7,
                    "title": "Atul Khatri Live in Kochi",
                    "short_title": null,
                    "slug": "atul-khatri-live-in-kochi",
                    "ticket_type": "Multiple Ticket",
                    "description": "<div class=\"event-details\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\">\r\n<div class=\"container\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: auto; padding: 24px; -webkit-box-flex: 1; flex: 1 1 100%; width: 1185px; max-width: 1185px;\">\r\n<div class=\"layout column wrap\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; display: flex; -webkit-box-flex: 1; flex: 1 1 auto; flex-flow: column wrap; min-width: 0px; -webkit-box-orient: vertical; -webkit-box-direction: normal;\">\r\n<div class=\"flex mt-4\" style=\"box-sizing: inherit; background-repeat: no-repeat; padding: 0px; -webkit-box-flex: 1; flex: 1 1 auto; max-width: 100%; margin: 24px !important 0px 0px 0px;\">\r\n<div style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px;\">\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; text-align: left;\">Can businessmen be funny? Yes. Meet Atul Khatri, a middle-aged businessman- turned-comedian who now makes a living making people laugh harder than they ever have. A past member of one of the country's leading comedy collectives, East India Comedy, Atul has appeared on their YouTube series like EIC Outrage, and specials such as EIC vs Bollywood. Bringing his 40+- year-old perspective with every show, he performs regularly at comedy clubs and does private shows in India and abroad. The comedian has showcased his skills at the prestigious Utrecht International Comedy Festival in the Netherlands and Belgium and at the 8th Annual Hong Kong International Comedy Festival in 2014. CNN-IBN recently rated him as one of the Top 20 Comedians in India to Watch Out For, post winning the competition CEOs Got Talent.</p>\r\n</div>\r\n</div>\r\n</div>\r\n</div>\r\n</div>\r\n<div class=\"host-details\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\">\r\n<div class=\"container\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: auto; padding: 24px; -webkit-box-flex: 1; flex: 1 1 100%; width: 1185px; max-width: 1185px;\">&nbsp;</div>\r\n</div>",
                    "host_details": "<p><span style=\"color: rgba(0, 0, 0, 0.87); font-family: arial, helvetica, sans-serif; font-size: 10pt;\">Las Viegas Comedy Club (LVC) is proud to present its second show of the year in Kochi with none other than Atul Khatri</span><br style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\" /><span style=\"color: rgba(0, 0, 0, 0.87); font-family: arial, helvetica, sans-serif; font-size: 10pt;\">This election season, get ready to laugh your lungs with none other than Atul Khatri performing in Kochi</span></p>",
                    "itinerary": "",
                    "cancellation_policy": "",
                    "start_time": "2019-05-18T19:30:00.000000Z",
                    "end_time": "2019-05-18T21:30:00.000000Z",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    },
                    "booking": {
                        "type": "Bookable",
                        "button_text": "Book Now",
                        "external_url": "None"
                    },
                    "category": {
                        "category_id": 2,
                        "name": "Standup Comedy",
                        "slug": "standup-comedy",
                        "weight": 1
                    },
                    "gallery": [
                        {
                            "id": 5,
                            "category_type": "IMG",
                            "category_name": "Atul Khatri Kochi",
                            "upload": "http://13.234.60.82/media/Catagory_Atul%20Khatri%20Kochi/atul-khatri.jpg"
                        }
                    ],
                    "get_original": "/media/Events/1557827365/untitled_design__10_.png",
                    "medias": {
                        "thumbnail": "http://13.234.60.82/media/Events/1557827365/untitled_design__10__100x100.jpg",
                        "medium": "http://13.234.60.82/media/Events/1557827365/untitled_design__10__300x300.jpg",
                        "large": "http://13.234.60.82/media/Events/1557827365/untitled_design__10_.png"
                    },
                    "slots": [
                        {
                            "start_time": "2019-05-18T19:30:00.000000Z",
                            "end_time": "2019-05-18T21:30:00.000000Z",
                            "max_size": 1000,
                            "slotpc_set": [
                                {
                                    "seating_id": "409049d5-dc7c-40f7-b5ef-4e36cf4f4e5b",
                                    "price_cat": {
                                        "id": 7,
                                        "title": "Silver",
                                        "description": "GST Included",
                                        "price": 499,
                                        "false_price": 0,
                                        "max_size": 100,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 100,
                                    "limitCategory": 100,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 7,
                                    "slot": 7
                                },
                                {
                                    "seating_id": "af84ccdc-fc83-42ae-857d-4998256a9c09",
                                    "price_cat": {
                                        "id": 8,
                                        "title": "Gold",
                                        "description": "GST Included",
                                        "price": 699,
                                        "false_price": 0,
                                        "max_size": null,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 1000,
                                    "limitCategory": null,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 7,
                                    "slot": 7
                                },
                                {
                                    "seating_id": "d1a435e7-29f3-4df6-90db-887d685ef8f6",
                                    "price_cat": {
                                        "id": 9,
                                        "title": "Platinum",
                                        "description": "GST included",
                                        "price": 999,
                                        "false_price": 0,
                                        "max_size": null,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 1000,
                                    "limitCategory": null,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 7,
                                    "slot": 7
                                },
                                {
                                    "seating_id": "2ba4e27b-4e6f-41ec-8511-6a3e6f461c17",
                                    "price_cat": {
                                        "id": 10,
                                        "title": "Premium",
                                        "description": "GST Included",
                                        "price": 1199,
                                        "false_price": 0,
                                        "max_size": null,
                                        "additional_charge": 0,
                                        "additional_charge_label": null
                                    },
                                    "booked_seats": 0,
                                    "remaining_seats": 1000,
                                    "limitCategory": null,
                                    "limitSlot": 1000,
                                    "totalSlot": 1000,
                                    "event": 7,
                                    "slot": 7
                                }
                            ]
                        }
                    ],
                    "address_venue": {
                        "title": "The Regent Hall",
                        "label": "MG Road, Kochi",
                        "capacity": 200,
                        "rate": null,
                        "about": "<p style=\"margin: 0px 0px 16px; padding: 0px; border: 0px; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-stretch: inherit; font-size: 13.008px; line-height: 1.5em; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; outline: 0px; color: #7b7168;\"><span style=\"color: #000000;\">The Avenue Regent is located in the heart of the city with 60 luxury rooms, a tapas bar and houses one of the best cafes in town. The recently renovated Regent Hall is spacious and grand with high ceilings and silk wall-panellings. This pillar-less hall is ideal for wedding receptions and large conferences accommodating up to 200 seats in a theatre-style arrangement.</span></p>\r\n<p><strong><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">Valet parking available</span></strong></p>",
                        "type": {
                            "id": 3,
                            "title": "Indoor Hall"
                        },
                        "upload": [
                            {
                                "id": 5,
                                "image_name": "Regent Hall",
                                "upload": "http://13.234.60.82/media/VenuePhotos/Regent%20Hall/regent_hall.jpg"
                            }
                        ],
                        "location": {
                            "place": "The Avenue Regent, Mahatma Gandhi Road, Jos Junction, Pallimukku, Kochi, Kerala, India",
                            "latitude": 9.966751,
                            "longitude": 76.28666199999998
                        },
                        "slug": "the-regent-hall",
                        "city": {
                            "name": "Kochi",
                            "short_name": "KOK",
                            "slug": "kochi",
                            "payment_method": "PAYTM"
                        }
                    },
                    "artists": [
                        {
                            "id": 4,
                            "artistImage": [],
                            "artistSong": [],
                            "city": {
                                "name": "Kochi",
                                "short_name": "KOK",
                                "slug": "kochi",
                                "payment_method": "PAYTM"
                            },
                            "title": "Atul Khatri",
                            "thumbnail": "http://13.234.60.82/media/Artist/Atul%20Khatri/atul.jpg",
                            "slug": "atul-khatri",
                            "fb_followers": 297000,
                            "inst_followers": 127500,
                            "rate": null,
                            "about": "<div class=\"event-details\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\">\r\n<div class=\"container\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: auto; padding: 24px; -webkit-box-flex: 1; flex: 1 1 100%; width: 1185px; max-width: 1185px;\">\r\n<div class=\"layout column wrap\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; display: flex; -webkit-box-flex: 1; flex: 1 1 auto; flex-flow: column wrap; min-width: 0px; -webkit-box-orient: vertical; -webkit-box-direction: normal;\">\r\n<div class=\"flex mt-4\" style=\"box-sizing: inherit; background-repeat: no-repeat; padding: 0px; -webkit-box-flex: 1; flex: 1 1 auto; max-width: 100%; margin: 24px !important 0px 0px 0px;\">\r\n<div style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px;\">\r\n<p style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px 0px 16px; padding: 0px;\"><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">Can businessmen be funny? Yes. Meet Atul Khatri, a middle-aged businessman- turned-comedian who now makes a living making people laugh harder than they ever have. A past member of one of the country's leading comedy collectives, East India Comedy, Atul has appeared on their YouTube series like EIC Outrage, and specials such as EIC vs Bollywood. Bringing his 40+- year-old perspective with every show, he performs regularly at comedy clubs and does private shows in India and abroad. The comedian has showcased his skills at the prestigious Utrecht International Comedy Festival in the Netherlands and Belgium and at the 8th Annual Hong Kong International Comedy Festival in 2014. CNN-IBN recently rated him as one of the Top 20 Comedians in India to Watch Out For, post winning the competition CEOs Got Talent.</span></p>\r\n</div>\r\n</div>\r\n</div>\r\n</div>\r\n</div>\r\n<div class=\"host-details\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: 0px; padding: 0px; color: rgba(0, 0, 0, 0.87); font-family: Roboto, sans-serif;\">\r\n<div class=\"container\" style=\"box-sizing: inherit; background-repeat: no-repeat; margin: auto; padding: 24px; -webkit-box-flex: 1; flex: 1 1 100%; width: 1185px; max-width: 1185px;\">&nbsp;</div>\r\n</div>"
                        }
                    ],
                    "lowest_price": 499
                }
            ]
        }
    ],
    "featurevenue": [
        {
            "name": "Venues in Kochi",
            "slug": "venues-in-kochi",
            "id": 1,
            "city": 1,
            "venue": [
                {
                    "title": "Crowne Plaza Kochi",
                    "label": "",
                    "capacity": 150,
                    "rate": 123,
                    "about": "<p><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span><span style=\"color: #4a4a4a; font-family: Arial, Tahoma, 'Bitstream Vera Sans', sans-serif; font-size: 16px;\">Crowne Plaza Kochi is ideally located on the NH 47 Bypass and provides easy access to the major business arenas,city centre and the widely acclaimed Fort Kochi. The hotel is just 33 kms away from the International Airport, 5 kms from the railway station and 8 kms from the major shopping malls in the city. The hotel has 269 spacious business rooms and suites with panoramic views of the backwaters and the city.Our variety of authentic culinary outlets, extensive spa, leisure facilities, and well equipped meeting rooms for up to 900 all within a tranquil waterfront setting making Crowne Plaza Kochi the preferred International brand for business, leisure and events.</span></p>",
                    "type": {
                        "id": 1,
                        "title": "Resort"
                    },
                    "upload": [
                        {
                            "id": 1,
                            "image_name": "image1",
                            "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                        }
                    ],
                    "location": {
                        "place": "Crowne Plaza Kochi, Kundannoor, Junction, Kochi, Kerala, India",
                        "latitude": 9.9341165,
                        "longitude": 76.31893739999998
                    },
                    "slug": "crowne-plaza-kochi",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    }
                },
                {
                    "title": "Hilida in hghghvgv vhvhvhg",
                    "label": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop p",
                    "capacity": 1999,
                    "rate": 2000000,
                    "about": "<p><strong style=\"margin: 0px; padding: 0px; font-family: 'Open Sans', Arial, sans-serif; text-align: justify;\">Lorem Ipsum</strong><span style=\"font-family: 'Open Sans', Arial, sans-serif; text-align: justify;\">&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</span></p>\r\n<p><strong style=\"margin: 0px; padding: 0px; font-family: 'Open Sans', Arial, sans-serif; text-align: justify;\">Lorem Ipsum</strong><span style=\"font-family: 'Open Sans', Arial, sans-serif; text-align: justify;\">&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</span></p>",
                    "type": {
                        "id": 2,
                        "title": "luxury hotel"
                    },
                    "upload": [
                        {
                            "id": 1,
                            "image_name": "image1",
                            "upload": "http://13.234.60.82/media/VenuePhotos/image1/presidential-suite--v16572936.jpg"
                        },
                        {
                            "id": 2,
                            "image_name": "Holiday inn",
                            "upload": "http://13.234.60.82/media/VenuePhotos/Holiday%20inn/Collabo_logo_plus_text_screenshot.png"
                        },
                        {
                            "id": 3,
                            "image_name": "goliday in2",
                            "upload": "http://13.234.60.82/media/VenuePhotos/goliday%20in2/Highhopes.png"
                        },
                        {
                            "id": 4,
                            "image_name": "rj",
                            "upload": "http://13.234.60.82/media/VenuePhotos/rj/mm.jpg"
                        }
                    ],
                    "location": {
                        "place": "Holiday Inn, Chakkaraparambu, Vennala, Kochi, Kerala, India",
                        "latitude": 9.990196899999997,
                        "longitude": 76.31594589999997
                    },
                    "slug": "hilida-in-hghghvgv-vhvhvhg",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    }
                },
                {
                    "title": "The Regent Hall",
                    "label": "MG Road, Kochi",
                    "capacity": 200,
                    "rate": null,
                    "about": "<p style=\"margin: 0px 0px 16px; padding: 0px; border: 0px; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-stretch: inherit; font-size: 13.008px; line-height: 1.5em; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; outline: 0px; color: #7b7168;\"><span style=\"color: #000000;\">The Avenue Regent is located in the heart of the city with 60 luxury rooms, a tapas bar and houses one of the best cafes in town. The recently renovated Regent Hall is spacious and grand with high ceilings and silk wall-panellings. This pillar-less hall is ideal for wedding receptions and large conferences accommodating up to 200 seats in a theatre-style arrangement.</span></p>\r\n<p><strong><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">Valet parking available</span></strong></p>",
                    "type": {
                        "id": 3,
                        "title": "Indoor Hall"
                    },
                    "upload": [
                        {
                            "id": 5,
                            "image_name": "Regent Hall",
                            "upload": "http://13.234.60.82/media/VenuePhotos/Regent%20Hall/regent_hall.jpg"
                        }
                    ],
                    "location": {
                        "place": "The Avenue Regent, Mahatma Gandhi Road, Jos Junction, Pallimukku, Kochi, Kerala, India",
                        "latitude": 9.966751,
                        "longitude": 76.28666199999998
                    },
                    "slug": "the-regent-hall",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    }
                },
                {
                    "title": "The Grant Conference Hall",
                    "label": "The Classik Fort",
                    "capacity": 500,
                    "rate": null,
                    "about": "<p><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">The Classik Fort Hotel offers five convention spaces for various purposes including both formal and informal events. The Ceremony Convention Hall has a 3200 square feet can accommodate 500 people in the classroom and 1000 people in floating crowd style.</span></p>\r\n<p><span style=\"font-family: arial, helvetica, sans-serif; font-size: 10pt;\">The Grant Conference Hall (2100 square feet), Regent Banquet Hall (1400 square feet) and Senate Hall (1200 square feet) can accommodate 350, 250 and 150 people in the classroom style and 500, 300 and 200 people in the floating crowd consecutively. For your audio/visual needs, the hotel is also equipped with the latest technology including projector, wireless hand-held microphones.&nbsp;</span></p>",
                    "type": {
                        "id": 3,
                        "title": "Indoor Hall"
                    },
                    "upload": [
                        {
                            "id": 6,
                            "image_name": "Classic Fort",
                            "upload": "http://13.234.60.82/media/VenuePhotos/Classic%20Fort/The-Classik-Fort-IMG-20151023-WA0011.jpg"
                        }
                    ],
                    "location": {
                        "place": "The Classik Fort, Thripunithura - Maradu Road, Gandhi Square, Poonithura, Maradu, Kochi, Kerala, India",
                        "latitude": 9.943833,
                        "longitude": 76.33528100000001
                    },
                    "slug": "the-grant-conference-hall",
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": "PAYTM"
                    }
                }
            ]
        }
    ]
    
    
    
    
##9 Order API- generic D for payfort , free events etails
http://13.234.60.82/api/generic-order/
Request Data
    {
    
    "event":8,
    "slot": 11,
    "payment":"payfort",
    
    "cust_name":"jib",
    "cust_email":"naseem.10@gmail.com",
    "cust_phone":"9947267251",
    
    "is_order_seller":false,
    
    
    
    "grandtotal":1.00,
     "io_id": [{"item_id":11,"item_name":"Early Bird Entry","item_price":1.00,"count":1,"pc_cat":11,"pc_slot":"0e65fc27-e698-484a-92d4-673812fab885","additional_charge":0}],
    
     "order_no":"409049d5-dc7c-40f7-b5ef-4e36cf4f4e5b"
    }


Response
{
    "order_details": {
        "event": 8,
        "slot": 11,
        "cust_name": "jib",
        "cust_email": "naseem.10@gmail.com",
        "cust_phone": "9947267251",
        "payment_method": null,
        "ordercreatedtime": "2019-08-23T12:46:44.314506Z",
        "grandtotal": 100,
        "io_id": [
            {
                "item_name": "Early Bird Entry",
                "pc_cat": 11,
                "pc_slot": "0e65fc27-e698-484a-92d4-673812fab885",
                "count": 1,
                "item_price": 1,
                "additional_charge": 0
            }
        ],
        "order_no": "rcptId4sSENTQ55QJW3f8noRr2uN",
        "payment_status": "Payment Pending",
        "order_status": "Order Completed",
        "id": "9841a577-5aa4-4646-8078-61b2e5cf8284",
        "ticket_code": "167108",
        "seller": null,
        "is_order_seller": false
    },
    "status": true
}

Here "order_no": "rcptId4sSENTQ55QJW3f8noRr2uN", is merchant reference for payfort
and order id  is "id": "9841a577-5aa4-4646-8078-61b2e5cf8284",

http://13.234.
60.82/api/ticket/?code=35D4A3


Response
{
    "status": 200,
    "bookinginfo": [
        {
            "thumbnail": "https://getcollabo-assetsserver.s3.amazonaws.com/media/Kochi%20Tech%20Summit/event_63d24f41e9e6d96370a892d99354556f_cbGVZi3.jpg",
            "location": "9.943833,76.33528100000001",
            "event": "Kochi Tech Summit",
            "address_venue": "The Classik Fort, Thripunithura - Maradu Road, Gandhi Square, Poonithura, Maradu, Kochi, Kerala, India",
            "start_time": "09:30:00",
            "end_time": "17:30:00",
            "things_to_know": [
                {
                    "id": 1,
                    "name": "drinks"
                }
            ],
            "slot": "Sunday 29 September, 2019",
            "slotend": "Sunday 29 September, 2019",
            "host_details": "",
            "cust_name": "Jobin Paul",
            "cust_email": "jobinpaul44@gmail.com",
            "cust_phone": "8921964470",
            "payment_method": null,
            "ordercreatedtime": "2019-09-27T16:33:59.908959Z",
            "grandtotal": 100,
            "io_id": [
                {
                    "item_name": "Early Bird Entry",
                    "pc_cat": 11,
                    "pc_slot": "c8dbbb9e-e142-4821-bb4c-38643374516e",
                    "count": 1,
                    "item_price": 1,
                    "additional_charge": 0
                }
            ],
            "order_no": "rcptIdgwTTuPG7DhnRV4Ax3u2Kef",
            "payment_status": "Payment Complete",
            "order_status": "OC",
            "id": "8238ff35-147e-437c-bec5-40ab42d118a1",
            "ticket_code": "35D4A3",
            "ticket_type": "Bookable",
            "seller": null,
            "is_order_seller": false
        }
    ],
    "relatedartist": [
        {
            "artists": [
                {
                    "id": 7,
                    "artistImage": [
                        {
                            "id": 19,
                            "image_name": "Motherjane",
                            "upload": "https://getcollabo-assetsserver.s3.amazonaws.com/media/ArtistPhotos/Motherjane/785219_Wallpaper2_Cropped.jpg"
                        },
                        {
                            "id": 20,
                            "image_name": "Motherjane",
                            "upload": "https://getcollabo-assetsserver.s3.amazonaws.com/media/ArtistPhotos/Motherjane/dc-Cover-0lpro94nm0k4bjbmhn7i2pt173-20170901062213.Medi_Cropped.jpg"
                        },
                        {
                            "id": 21,
                            "image_name": "Motherjane",
                            "upload": "https://getcollabo-assetsserver.s3.amazonaws.com/media/ArtistPhotos/Motherjane/DSC_0061_Cropped.jpg"
                        }
                    ],
                    "artistSong": [
                        {
                            "id": 8,
                            "image_name": "Broken",
                            "upload": "https://www.youtube.com/watch?v=a0QbmHvXqzI&feature=youtu.be",
                            "links": "YT"
                        }
                    ],
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": [
                            {
                                "id": 1,
                                "name": "payfort",
                                "slug": "payfort"
                            },
                            {
                                "id": 2,
                                "name": "freeevent",
                                "slug": "freeevent"
                            }
                        ]
                    },
                    "title": "Motherjane",
                    "thumbnail": "https://getcollabo-assetsserver.s3.amazonaws.com/media/Artist/Motherjane/153_Cropped_0ShvBXU.jpg",
                    "slug": "motherjane",
                    "fb_followers": 11000,
                    "inst_followers": 2000,
                    "rate": null,
                    "about": "<p>One of the oldest and most influential bands in India, Motherjane progressed the idea of fusing rock with Indian music, forming the Ethnic Rock genre. They are a household name in almost all parts of the country, with more than 2 decades of music making experience to their credit. Since their formation, they have released 2 studio albums and 5 singles, and one of the albums titled &lsquo;Maktub&rsquo; went on to win the &lsquo;Album of The Year&rsquo; title from Rolling Stone India in 2009.</p>",
                    "genre": null
                },
                {
                    "id": 9,
                    "artistImage": [
                        {
                            "id": 27,
                            "image_name": "Dj Sekhar",
                            "upload": "https://getcollabo-assetsserver.s3.amazonaws.com/media/ArtistPhotos/Dj%20Sekhar/18-guess-who-is-the-villain-in-gangster-movie_Cropped.jpg"
                        },
                        {
                            "id": 119,
                            "image_name": "dj sekhar",
                            "upload": "https://getcollabo-assetsserver.s3.amazonaws.com/media/ArtistPhotos/dj%20sekhar/img_5c45402ca6651b052d42889ef140e527_1498139980135_processed_orig_664lHX8.jpg"
                        }
                    ],
                    "artistSong": [
                        {
                            "id": 39,
                            "image_name": "Star Jam: Sekhar Menon",
                            "upload": "https://www.youtube.com/watch?v=v-1H3mG5TbY",
                            "links": "YT"
                        }
                    ],
                    "city": {
                        "name": "Kochi",
                        "short_name": "KOK",
                        "slug": "kochi",
                        "payment_method": [
                            {
                                "id": 1,
                                "name": "payfort",
                                "slug": "payfort"
                            },
                            {
                                "id": 2,
                                "name": "freeevent",
                                "slug": "freeevent"
                            }
                        ]
                    },
                    "title": "DJ Sekhar",
                    "thumbnail": "https://getcollabo-assetsserver.s3.amazonaws.com/media/Artist/DJ%20Sekhar/DJ_Sekhar_Menon.jpg",
                    "slug": "dj-sekhar",
                    "fb_followers": 4300,
                    "inst_followers": 72000,
                    "rate": null,
                    "about": "<p>In the electronic music scene for the past 11 years, Dj Sekhar has not only made a name for himself in the country but also abroad. He started his career in a small pub back in 2001, and since then has seen success in a tremendous amount. He made sure to follow his passion in the best possible way, by studying sound engineering. Now, he not only produces soundtracks for movies but also runs a Dj school of his own. A passionate and highly focused artist, Sekhar plans to make his own music and perform live across cities.</p>",
                    "genre": null
                }
            ]
        }
    ]
}
