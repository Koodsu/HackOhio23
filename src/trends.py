def make_graph(location):
    import openai
    from dotenv import load_dotenv
    import os
    load_dotenv()


    import pandas as pd
    import matplotlib.pyplot as plt

    openai.api_key = os.getenv('OPENAI_API_KEY')
    model_engine = "gpt-3.5-turbo"

    #max_tokens = 100

    def getGPTResponse(role, text):
        message = [{"role" : role, "content" : text}]

        completion = openai.ChatCompletion.create(
            model=model_engine,
            messages = message
        )

        return completion.choices[0]['message']["content"]

    '''name = input("Name: ")
    age = input("Age: ")'''

    #prompt = f"{name} is a {age} year old who lives in {location}. Give me some trends about climate change where he lives and a list of things (specific to where he lives) he can do to help the climate where he lives "

    emissions = getGPTResponse("system", f"co2 emissions in {location} in ppm from 2000 to 2019 (sample csv file format)")

    f = open("co2_emissions.csv", "a")
    f.write(emissions)
    f.close()

    data = pd.read_csv("co2_emissions.csv")
    df = pd.DataFrame(data)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])
    plt.bar(X, Y, color='g')

    plt.xlabel('Year')
    xticklist = range(2000, 2021,2)
    plt.xticks(xticklist)
    plt.ylabel('CO2 Emissions (million metric tons)')
    plt.title(f"CO2 Emissions in {location} from 2000 to 2019")

    # Show the graph
    #plt.show()
    plt.savefig('src/static/emissions_trend.png')

    f = open("co2_emissions.csv", "w")
    f.write("")
    f.close()


