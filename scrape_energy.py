# Import dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time
from splinter import Browser
from flask import Flask, jsonify, render_template

def scrape():
    # Extract population data
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/335rank.html'
    
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_abbr = []
    country_pop = []
    population_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        abbr = i.get("id")
        country_abbr.append(abbr)
        
        population = i.findAll("td")[2].text
        population = "".join(population.split(","))
        country_pop.append(float(population))
        
        rank = i.findAll("td")[0].text
        population_rank.append(rank)

    population_df = pd.DataFrame({
        "name": country_name,
        "abbr": country_abbr,
        "population": country_pop,
        "population_rank": population_rank
    })


    #Extract electricity consumption data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/253rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_econsumption = []
    econsumption_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        econsumption = i.findAll("td")[2].text
        econsumption = "".join(econsumption.split(","))
        country_econsumption.append(float(econsumption))
        
        rank = i.findAll("td")[0].text
        econsumption_rank.append(rank)

    econsumption_df = pd.DataFrame({
        "name": country_name,
        "econsumption": country_econsumption,
        "econsumption_rank": econsumption_rank
    })

    # Extract electricity from fossil fuel data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/257rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_fossil = []
    fossil_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        fossil = i.findAll("td")[2].text
        country_fossil.append(float(fossil))
        
        rank = i.findAll("td")[0].text
        fossil_rank.append(rank)

    fossil_df = pd.DataFrame({
        "name": country_name,
        "fossil": country_fossil,
        "fossil_rank": fossil_rank
    })


    # Extract electricity from nuclear fuels data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/258rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_nuclear = []
    nuclear_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        nuclear = i.findAll("td")[2].text
        country_nuclear.append(float(nuclear))
        
        rank = i.findAll("td")[0].text
        nuclear_rank.append(rank)

    nuclear_df = pd.DataFrame({
        "name": country_name,
        "nuclear": country_nuclear,
        "nuclear_rank": nuclear_rank
    })


    # Extract electricity from hydroelectric plants data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/259rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_hydro = []
    hydro_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        hydro = i.findAll("td")[2].text
        country_hydro.append(float(hydro))
        
        rank = i.findAll("td")[0].text
        hydro_rank.append(rank)

    hydro_df = pd.DataFrame({
        "name": country_name,
        "hydroelectric": country_hydro,
        "hydro_rank": hydro_rank
    })


    # Extract electricity from other renewable sources data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/260rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_other = []
    other_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        other = i.findAll("td")[2].text
        country_other.append(float(other))
        
        rank = i.findAll("td")[0].text
        other_rank.append(rank)

    other_df = pd.DataFrame({
        "name": country_name,
        "other": country_other,
        "other_rank": other_rank
        
    })


    # Extract electricity from carbondioxide emissions from consumption of energy data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/274rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_emissions = []
    emissions_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        emissions = i.findAll("td")[2].text
        emissions = "".join(emissions.split(","))
        country_emissions.append(float(emissions))
        
        rank = i.findAll("td")[0].text
        emissions_rank.append(rank)

    emissions_df = pd.DataFrame({
        "name": country_name,
        "emissions": country_emissions,
        "emissions_rank": emissions_rank
    })


    # Extract GDP data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/208rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_gdp = []
    gdp_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow: 
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        gdp = i.findAll("td")[2].text
        gdp = "".join(gdp.split(","))
        country_gdp.append(float(gdp[1:]))
        
        rank = i.findAll("td")[0].text
        gdp_rank.append(rank)

    gdp_df = pd.DataFrame({
        "name": country_name,
        "gdp": country_gdp,
        "gdp_rank": gdp_rank
    })

    # Extract GDP per capita data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/211rank.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_gdppc = []
    gdppc_rank = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow: 
        name = i.find("td", class_="region").find("a").text
        country_name.append(name)
        
        gdppc = i.findAll("td")[2].text
        gdppc = "".join(gdppc.split(","))
        country_gdppc.append(float(gdppc[1:]))
        
        rank = i.findAll("td")[0].text
        gdppc_rank.append(rank)

    gdppc_df = pd.DataFrame({
        "name": country_name,
        "gdppc": country_gdppc,
        "gdppc_rank": gdppc_rank
})


    # Extract coordinates data
    url = 'https://www.cia.gov/library/publications/the-world-factbook/fields/277.html'
    browser.visit(url)

    time.sleep(3)

    html = browser.html

    soup = bs(html, "html.parser")

    country_name = []
    country_lat = []
    country_long = []

    tbody = soup.find("tbody")
    trow = tbody.findAll("tr")

    for i in trow:
        lat_long = []
        
        try:
            coord = i.find("div", {"id": "field-geographic-coordinates"})\
                .find("div", class_ = "category_data subfield text").text.strip()
            lat_long = coord.split(",")
            
            if lat_long[0][-1] == "S":
                lat = -float(lat_long[0][:-2].replace(" ", "."))
            else:
                lat = float(lat_long[0][:-2].replace(" ", "."))

            if lat_long[1][-1] == "W":
                long = -float(lat_long[1][1:-2].replace(" ", "."))
            else:
                long = float(lat_long[1][1:-2].replace(" ", "."))
            
            name = i.find("td", class_="country").find("a").text
            
            country_name.append(name)
            country_lat.append(lat)
            country_long.append(long)
            
        except:
            try:
                coord = i.find("div", {"id": "field-geographic-coordinates"})\
                    .find("div", class_ = "category_data subfield text").text.strip()
                
                search = re.search(':(.+?);', coord).group()
                if search != None:
                    try:
                        lat_long = search[2:-1].split(",")

                        if lat_long[0][-1] == "S":
                            lat = -float(lat_long[0][:-2].replace(" ", "."))
                        else:
                            lat = float(lat_long[0][:-2].replace(" ", "."))
                        

                        if lat_long[1][-1] == "W":
                            long = -float(lat_long[1][1:-2].replace(" ", "."))
                        else:
                            long = float(lat_long[1][1:-2].replace(" ", "."))

                        name = i.find("td", class_="country").find("a").text
                        
                        country_name.append(name)
                        country_lat.append(lat)
                        country_long.append(long)
                        
                    except:
                        print(f"Whoops! I'm stupid...")
                else:
                    print(f"Whoops! I'm stupid...")
            except:
                print(f"Whoops! I'm stupid...")
    
    coord_df = pd.DataFrame({
        "name": country_name,
        "lat": country_lat,
        "long": country_long
    })

    browser.quit()

    # Merge data
    merge1_df = population_df.merge(econsumption_df, on="name")
    merge2_df = merge1_df.merge(fossil_df, on="name")
    merge3_df = merge2_df.merge(nuclear_df, on="name")
    merge4_df = merge3_df.merge(hydro_df, on="name")
    merge5_df = merge4_df.merge(other_df, on="name")
    merge6_df = merge5_df.merge(emissions_df, on="name")
    merge7_df = merge6_df.merge(gdp_df, on="name")
    merge8_df = merge7_df.merge(gdppc_df, on="name")
    energy_df = merge8_df.merge(coord_df, on="name")

    # Convert DataFrame to a dictionary
    browser.quit()

    energy_dict = energy_df.to_dict("list")

    return energy_dict