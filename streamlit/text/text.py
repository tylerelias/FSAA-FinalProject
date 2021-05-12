# Quite a messy file with the texts in Icelandic

class Text:
    
    # The intro and header
    header = '# Niðurgreiðslureiknivél'
    intro_text = 'Tilgangurinn með þessari vefsíðu er að veita einstaklingum yfirsín yfir hversu mikill sparnaður felst í því að greiða inn á höfuðstól á láni. Það reynst bæði flókið og tímafrekt að gera svona útreikningar en þessi vefsíða er ætluð til þess að einfalda ferlið.'
    
    # for lines
    line = '---' 
    
    # For the first step when selecting a loan type
    step_1 = '1. Byrjaðu á því að velja tegund láns'
    loan_type = 'Tegund Láns:'
    none_selected =  'Ekkert valið'
    indexed = 'Verðtryggt'
    non_indexed = 'Óverðtryggt'

    # For the second step
    selected_non_indexed = '### Þú valdir **Óverðtryggt** lán'
    selected_indexed = '### Þú valdir **Verðtryggt** lán'
    step_2 = '2. Fylltu út eftirfarandi reiti, ef þú ert í einhverjum vafa getur þú alltaf smellt á spurningarmerkið \'?\' hægra meginn við reitina til þess að fá íterlegri úpplýsingar um þann reit.'
    
    loan_amount = 'Núverandi upphæð láns'
    amount_help = 'Sú heildar upphæð sem eftir á að greiða. Dæmi: Tíu milljón króna lán skal vera fyllt inn sem \'10000000\' í þennan reit'
    
    interest_rate = 'Núverandi vextir'
    interest_rate_help = 'Vextirnir á láninu. Ef þú ert ekki viss um hvað þeir eru getur þú nálgast þá í heimabankanum þínum með því að fara í lánsyfirlitið. Dæmi: Ef lánið er með 1.23% vöxtum skal setja \'1.23\' í þennan reit'

    inflation_rate = 'Núverandi verðbólga'
    inflation_rate_help = 'Verðbólga er breytileg og getur hækkað og lækkað í framtíðinni. Það er hægt að nálgast núverandi verbólgu á heimasíðu Seðlabanka Íslands: https://www.sedlabanki.is/ en þess má til gamans geta að verðbólgumarkmið seðlabankans er ávalt 2.5%. Dæmi: Ef verðbólgan er 2.5% skal setja 2.5 í reitinn.'
    
    duration = 'Lánstími eftir (í mánuðum)'
    duration_help = 'Lánstími er fjöldi skipta sem þú átt eftir að greiða inn á lánið. Það er hægt að nálgast þessa tölu í heimabankanum þínum með því að fara í lánsyfirlitið. Dæmi: Ef þú ert með lán sem hefur 25 ára lánstíma þá eru það 300 mánuðir í heildina (25 ár * 12 mánuður í hverju ári = 300 mánuðir), þannig að í þennan reit myndir þú setja 300'
    
    done = 'Allir reitir fylltir? Smelltur hér'