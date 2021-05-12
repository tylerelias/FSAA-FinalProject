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
    submit = 'Staðfesta Upplýsingar'

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

    # Step 3
    step_3 = '3. Hér fyrir neðan hefur verið reiknað út hvað þú munt enda með að greiða í heildina til banksans fyrir íbúðarlánið. Í flestum tilfellum endar þú með að greiða margar milljónir í vaxtarkostnað, en með því að greiða aukalega beint inn á höfuðstól lánsins er hægt að stórlækka þessa tölu. Við munum fara betur yfir það í 4. skrefi'
    if_wrong_input = 'Ath: Ef þú slóst inn einvherjar vitlausar upplýingar getur þú einfaldlega lagað það í 2. skrefi og smellt aftur takkann til að fá út nýja útreikninga'
    total_loan_payment = 'Samtals Greitt'
    total_interest_payment = 'Samtals Greiddir Vextir'
    monthly_payments = 'Mánaðalegar Greiðslur'
    stop_getting_ripped_off = 'Þessir útreikingar gera ráð fyrir að þú greiðir aldrei inn á höfuðstól lánsins. Í næsta skrefi munum við kanna tvær leiðir til þess að minnka heildar vaxargreiðlur til bankanna, en það getur verið sparnaður upp á margar milljónir.'
    radio_pay_fixed_rate = 'Borga fasta greiðslu inn á höfuðstól lánsins'
    radio_pay_adjusted_rate = 'Borga aðlagandi greiðslu inn á höfuðstól'

    # Step 4
    btn_step4 = 'Smelltu hér til að fara í 4. skref'
    step_4 = '4. Hér getur þú gert áætlun um mánaðarlegar greiðslur inn á höfuðstól lánsins, en með því að borga mánaðarlega inn á höfuðstólinn getur þú sparað margar milljónir í vaxtargreiðslur og líka greitt up lánið fyrr.'

    reset = 'Núllstilla'