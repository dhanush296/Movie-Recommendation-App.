import gradio as gr
import random

movies_by_genre = {
    "Action": ["Gabbar Singh", "Aravinda Sametha Veera Raghava", "Sahoo", "Akhanda", "Devara", "Narappa","Bhemala Nayak","Chatrapathi","Pushpa: The Rule-2","Pokiri","Jawan","Major","Baashha","Vishwaroopam","Leo","Thani Oruvan","Thuppakki","Kaithi", "Ayyappanum Koshiyum", "Kurup", "Bheeshma Parvam", "Kalki"],
    "Comedy": ["Nuvvu Naaku Nachchav", "Pelli Choopulu", "Jathi Ratnalu", "Ee Nagaraniki Emaindi", "Tillu Square", "Love Today", "Joker", "Nanban", "Remo", "Don", "Prince", "Mark Antony", "Guruvayoor Ambalanadayil", "Kunjiramayanam (2015)", "Android Kunjappan Ver 5.25 (2019)", "Salt N' Pepper", "Oru Vadakkan Selfie", "Aavesham"],
    "Drama": ["Lucky Baskhar", "Rangasthalam", "Pratinidhi 2", "Oopiri", "C/o Kancharapalem","Mr.Perfect","Vada Chennai","Pushpa:The Rise-1","Animal","Yeh jawani hai deewani","Nayagan","Dhalapathy","Company","Rakta charitra","Satya","Sarkar","Mohabattein","Forrest gump","Good fellas","Godfather","The wolf of the street","Jailer","Varun Doctor","Good Night","Aramm","Soodhu Kavvum","Dada","Ayothi","Maaveeran","Chithha", "Premam", "Kumbalangi Nights", "The Great Indian Kitchen", "Take Off"],
    "Horror": ["Masooda", "Virupaksha", "Maa Oori Polimera", "Kanchana", "Taxiwala", "Bhaagamathie","Chandramukhi","Demonte Colony 2","Prema Katha Chitram","Raju Gari Gadhi","Dayam","Pizza","Maya","Thuneri", "Ezra", "Neelavelicham", "Pretham"],
    "Sci-Fi": ["Aditya 369","Antariksham 9000KMPH","Kaliki 2898-AD", "Oke Oka Jeevitham", "Ismart Shankar", "Adbhutham", "Maanaadu","Tic-Tic-Tic","Robo","ra one","Interstellar","Tenet","Oppenheimer","Inception","The prestige","Memento","Insomnia", "Android Kunjappan Ver 5.25", "Minnal Murali (2021)", "Varathan"],
    "Family": ["Murari", "Srikaram", "Balagam", "F2", "Srimanthudu", "Seethamma Vakitlo Sirimalle Chettu", "Ala Vaikunthapurramuloo", "Samajavaragamana","S/o Sathyamuruty","Guntur Karam","Papanasam","Deiva Thirumagal","Surya Vamsam","Meiyazhagan","Kadaikutty Singam","Uttama Puthiran","Varisu","Sivappu manjal pachai", "Jacobinte Swargarajyam", "Ustad Hotel", "C/o Saira Banu"],
    "Love": ["Orange", "Tholi Prema", "Kushi", "Sita Ramam", "Colour Photo", "Radhe Shyam", "Jaanu", "Shyam Singha Roy", "Arjun Reddy", "Joe","Uppena","Hi Nanna","Premam","Darling","Ok jaanu","Aei dil hai mushkil","Rockstar","Wake up sid","Tamasha","Dil se","Roja","Geethanjali","Mounaragam","Tuu jhooti mai makhar","Bombay","Ok kanmani","Rangeela","Dilwale dil le jayenge","Chennai express","Om shanti om","Mai hoon na","Devdas","Veer-zarra","Zero","Alaipayuthey","96","Sethu","Vinnaithaandi Varuvaayaa","Moondram Pirai","Thulladha Manamum Thullum","Minnale","Pariyerum Perumal","Kaadhal","Raja Rani","7G Rainbow Colony"],
    "Thriller": ["Drishyam", "Hit", "Mathu Vadhalara", "Agent Sai Srinivasa Athreya", "Kshanam", "Rakshahudu", "V","Oka Kshnam","Gudachari","Avaru","Vikram","Gargi","Mahaan","Diary","Veeramae Vaagai Soodum","Cadaver","Ayirathil Oruvan","Por thozhil","Ratchasan","Imaikaa nodigal","Irumbu thirai", "Joji", "Forensic", "Iratta"],
    "Periodical": ["Bahubali-1&2", "Bimbisara", "Magadheera", "Gautamiputra Satakarni", "Rudhuramadevi", "Ghazi","RRR","Poniyan selvan 1-2"],
    "Friendship": ["Happydays", "Vunnadi Okate Zindagi", "Yevade Subramanyam", "Maharshi", "Kerintha", "Devadas", "Kirrak party", "Aarya 1&2","Salaar","Ee Nagaraniki Emaindi","3 idiots","Thoza","Priyamaana Thozhi","Friends","Endrendrum Punnagai","Chennai 28","Goa","Priyamana Thozhi","Nanban","Messaya Murukku", "Bangalore Days", "Om Shanti Oshana", "Thattathin Marayathu"]
}

previous_recommendations = []

def recommend_movie(genre):
    if genre in movies_by_genre:
        movies = movies_by_genre[genre]
        movies = [movie for movie in movies if movie not in previous_recommendations]
        if movies:
            recommendation = random.choice(movies)
            previous_recommendations.append(recommendation)
            return recommendation, gr.update(visible=True)
        else:
            return "No more recommendations available. Please select another genre.", gr.update(visible=False)
    else:
        return "Sorry, we don't have any recommendations for that genre.", gr.update(visible=False)

def handle_satisfaction(satisfied, genre):
    if satisfied == "Yes":
        return "Thanks for using Movie Recommendation App\nEnjoy the Movie", gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)
    else:
        recommendation, satisfaction_visibility = recommend_movie(genre)
        return recommendation, satisfaction_visibility, gr.update(visible=True), gr.update(visible=False)

def reset_recommendations():
    global previous_recommendations
    previous_recommendations = []
    return "Recommendations reset. You can start over.", gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def handle_rating(rating):
    return f"Thanks for rating the app as {rating}!", gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)

genre_list = list(movies_by_genre.keys())

with gr.Blocks() as demo:
    gr.Markdown("# Movie Recommendation App")
    genre = gr.Dropdown(label="Select a genre", choices=genre_list)
    recommend_button = gr.Button("Recommend a Movie")
    recommendation = gr.Textbox(label="Recommended Movie")
    satisfaction = gr.Radio(label="Are you satisfied with the recommendation?", choices=["Yes", "No"], visible=False)
    rate_app = gr.Radio(label="Please rate the app:", choices=["Good", "Average", "Bad"], visible=False)
    thank_you_note = gr.Markdown("", visible=False)
    reset_button = gr.Button("Reset Recommendations")

    recommend_button.click(recommend_movie, inputs=genre, outputs=[recommendation, satisfaction])
    satisfaction.change(handle_satisfaction, inputs=[satisfaction, genre], outputs=[recommendation, satisfaction, rate_app, thank_you_note])
    rate_app.change(handle_rating, inputs=rate_app, outputs=[thank_you_note, recommendation, satisfaction, rate_app, reset_button])
    reset_button.click(reset_recommendations, outputs=[recommendation, satisfaction, rate_app, thank_you_note, reset_button])

    gr.Markdown("Created by Dhanush for Python project")

demo.launch()
