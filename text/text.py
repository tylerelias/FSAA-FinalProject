# Quite a messy file with the texts in Icelandic

class Text:
    
    # The intro and header
    header = '# Niðurgreiðslureiknivél'
    intro_text = 'Tilgangurinn með þessari vefsíðu er að veita einstaklingum yfirsín yfir hversu mikill sparnaður felst í því að greiða inn á höfuðstól á láni. Það reynst bæði flókið og tímafrekt að gera svona útreikningar en þessi vefsíða er ætluð til þess að einfalda ferlið.'
    # Explain the diff between the two
    # TEMP ! Images:
    # https://i.ibb.co/gJTKKSr/indexed-more-exp.png
    # https://i.ibb.co/42rrCZ2/indexed.png
    # https://i.ibb.co/vPr9pDs/non-indexed.png

    index_vs_nonindex = """
    Megin munur á verðtryggðum og óverðtryggðum lánum er í stuttu máli að verðtryggð lán eru alltaf verri kosturinn þegar í heildina er litið.
    
    **Verðtryggð** lán fylgja verðbólgu í landinu. \
    Það þýðir að í flestum tilfellum mun skuldinn hækka í hverjum mánuði um tugi eða hundruð þúsundir króna, þó að viðkomandi sé að greiða lánið mánaðarlega. Það er vissulega hægt að finna nokkra mánuði síðustu áratugina þar sem verðbólgan er neikvæð og í þeim tilfellum hækkar höfuðstóll lánsins ekki, en það gerist mjög sjaldan.
    Það sem lætur verðtryggð lán líta vel út er að til að byrja með eru afborganir á þeim lánum lægri heldur en á óverðtryggðum lánum, en það er aðeins tilfellið í nokkur ár þar sem að mánaðarlega greiðslan hækkar í hverjum mánuði og tekur fram úr mánaðarlegum greiðslum óverðtryggðra lána innan nokkura ára.
    En á sama tíma eru greiðslur á óverðtryggðum lánum þau sömu (svo lengi sem að vextir á lánunum hækka ekki).

    
    [Sjá dæmi um óverðtryggt lán](https://i.ibb.co/vPr9pDs/non-indexed.png)

     - *Ath: Rauði kassinn með pílunni sýnir að ekkert bætist á höfuðstól lánsins, þannig að það greiðist niður með tímanum*

    [Sjá dæmi um verðtryggt lán](https://i.ibb.co/42rrCZ2/indexed.png)

    - *Ath: Rauði kassinn með pílunni sýnir að **verðbætur bætast** á höfuðstól lánsins, þannig að höfuðstólinn hækkar með tímanum. Þetta er mjög slæmt fyrir þann sem tekur lánið og þekkist ekki í öðrum löndum*

    [Sjá dæmi um hvenær afborganir á verðtryggðu láni verða hærri en óverðtryggða](https://i.ibb.co/gJTKKSr/indexed-more-exp.png)
    
    - *Eftir þrjú ár og fimm mánuði eru mánaðarlegar afborganir á verðtryggðu láni orðið hærra en hjá sambærilegu óvertryggðu láni, og það mun halda áfram að hækka þar til að er greitt að fullu*
    
    
    > **Gallar**:

    > 1. Verðtryggð lán eru þannig gerð til að líta út sem sá kostur sem býður lægri mánaðarlegar afborganir fyrir fólk sem vill borga sem minnst hvern mánuð. En raunin er sú að eftir nokkur ár verða afborganirnar hærri og viðkomandi endar með að greiða miklu meira til baka heldur en sá sem tekur óverðtryggt.
    
    
    > 2. Höfuðstóll lánsins hækkar í hverjum mánuði fyrsta helming lán tímans, þannig að þú endar með að skulda meiri fjárhæð heldur en þú fékkst lánað fyrir.
    
    > **Kostir**:
    
    > 1. Það eru einfaldlega engir kostir sem fylgja verðtryggðum lánum. Þó að afborganir séu vissulega lægri fyrstu árin, verða þau mikið hærri heldur en afborganir á óverðtryggðum lánum.

    **Óverðtryggð** lán byrja með því að hafa hærri mánaðarlegar greiðslur heldur en óverðtryggð lán og virka þannig sem óhagstæðari kostur. En eftir nokkur ár mun verðtryggða lánið hafa tekið fram úr því óverðtryggða.
    Það sem meira er þá hækkar aldrei höfuðstóll lánsins eins og gerist með verðtryggð lán, sem er frábært.

    
    > **Gallar**:

    > 1. Vaxtrarbreytingar geta haft áhrif á mánaðalegar afborganar. Núna eru vextir í sögulega lágmarki hjá Seðlabanka Íslands (0.75%) og margt sem að bendir til þess að þeir muni hækka á næstunni
    
    
    > 2. Afborganir á þessum lánum eru háar til að byrja með, en þar sem að þessi lán hækka ekki í takt við verðbólgu rétt eins og verðtryggð lán og laun flestra gera, þá mun þessi upphæð vera lægra hlutfall af tekjum einstaklings þegar lengra líður á láninu
    
    > **Kostir**:
    
    > 1. Þú getur sparað marga tugi milljóna í *verðbætur* sem einstaklingur sem tekur verðtryggt lán þarf að greiða

    > 2. Þú eignast fljótar hlut í eigninni þinni

    > 3. Laun hækka með tímanum skv. verðbólgu þannig að afborganir af láninu munu hafa minni áhrif á tekjuráðstöfunina þína


    """
    # for lines
    line = '---'
    
    # For the first step when selecting a loan type
    step_1 = '1. Byrjaðu á því að velja tegund láns'
    loan_type = 'Tegund Láns:'
    none_selected =  'Ekkert valið'
    indexed = 'Verðtryggt'
    non_indexed = 'Óverðtryggt'
    submit = 'Staðfesta Upplýsingar'
    n_idx_diff = 'Hver er munurinn á verðtryggðum og óverðtryggðum lánum?'

    # For the second step
    selected_non_indexed = '### Þú valdir **Óverðtryggt** lán'
    selected_indexed = '### Þú valdir **Verðtryggt** lán'
    step_2 = '2. Fylltu út eftirfarandi reiti, ef þú ert í einhverjum vafa getur þú alltaf smellt á spurningamerkið \'?\' hægra meginn við reitina til þess að fá ítarlegri upplýsingar um þann reit.'
    
    loan_amount = 'Núverandi upphæð láns'
    amount_help = 'Sú heildarupphæð sem eftir á að greiða. Dæmi: Tíu milljón króna lán skal vera fyllt inn sem \'10000000\' í þennan reit'
    
    interest_rate = 'Núverandi vextir'
    interest_rate_help = 'Vextirnir á láninu. Ef þú ert ekki viss um hvað þeir eru getur þú nálgast þá í heimabankanum þínum með því að fara í lánsyfirlit. Dæmi: Ef lánið er með 1.23% vöxtum skal setja \'1.23\' í þennan reit'

    inflation_rate = 'Núverandi verðbólga'
    inflation_rate_help = 'Verðbólga er breytileg og getur hækkað og lækkað í framtíðinni. Það er hægt að nálgast núverandi verðbólga á heimasíðu Seðlabanka Íslands: https://www.sedlabanki.is/ en þess má til gamans geta að verðbólgumarkmið seðlabankans er ávallt 2.5%. Dæmi: Ef verðbólgan er 2.5% skal setja 2.5 í reitinn.'
    
    duration = 'Lánstími eftir (í mánuðum)'
    duration_help = 'Lánstími er fjöldi skipta sem þú átt eftir að greiða inn á lánið. Það er hægt að nálgast þessa tölu í heimabankanum þínum með því að fara í lánsyfirlit. Dæmi: Ef þú ert með lán sem hefur 25 ára lánstíma þá eru það 300 mánuðir í heildina (25 ár * 12 mánuðir í hverju ári = 300 mánuðir), þannig að í þennan reit myndir þú setja 300'
    
    done = 'Allir reitir fylltir? Smelltu hér'

    # Step 3
    step_3 = '3. Hér fyrir neðan hefur verið reiknað út hvað þú munt enda með að greiða í heildina til bankans fyrir íbúðarlánið. Í flestum tilfellum endar þú með að greiða margar milljónir í vaxtakostnað, en með því að greiða aukalega beint inn á höfuðstól lánsins er hægt að stórlækka þessa tölu. Við munum fara betur yfir það í 4. skrefi'
    wrong_input = 'Settir þú inn rangar tölur?'
    if_wrong_input = """
    **Tímabundið: Vegna galla í kerfinu þarf að endurhlaða (refresh) síðuna og setja inn gögninn í skrefi 2 upp á nýtt. 
    Það er hægt með að ýta á F5 takkann á lyklaborðinu eða Refresh hnappinn á vafranum þínum. Við byðjumst afsökunar á þessum óþægindum**
    
    Ath: Ef þú slóst inn einhverjar vitlausar upplýsingar getur þú einfaldlega lagað það í 2. skrefi og smellt aftur takkann til að fá út nýja útreikninga
    """    
    total_loan_payment = 'Samtals Greitt'
    total_interest_payment = 'Samtals Greiddir Vextir'
    monthly_payments = 'Mánaðalegar Greiðslur'
    stop_getting_ripped_off = 'Þessir útreikningar gera ráð fyrir að þú greiðir aldrei inn á höfuðstól lánsins. Í næsta skrefi munum við kanna tvær leiðir til þess að minnka heildar vaxtagreiðslur til bankanna, en það getur verið sparnaður upp á margar milljónir.'
    radio_pay_fixed_rate = 'Borga fasta greiðslu inn á höfuðstól lánsins'
    radio_pay_adjusted_rate = 'Borga aðlaðandi greiðslu inn á höfuðstól'
    total_amount_with_interest = 'Lán með vöxtum samtals'

    # Step 4
    btn_step4 = 'Smelltu hér til að fara í 4. skref'
    step_4 = '4. Hér getur þú gert áætlun um mánaðarlegar greiðslur inn á höfuðstól lánsins, en með því að borga mánaðarlega inn á höfuðstólinn getur þú sparað margar milljónir í vaxtagreiðslur og líka greitt upp lánið fyrr.'
    pay_fixed_rate = 'Þú hefur valið að greiða **fastar greiðslur** inn á lánið. Vinsamlegast veldu þá upphæð sem að þú villt greiða mánaðarlega inn á lánið hérna fyrir neðan.'
    pay_fixed_rate_example = 'Dæmi: Þú ert að greiða mánaðarlega 150.000kr til bankans og er tilbúinn til þess að greiða ávallt 50.000kr inn á höfuðstól lánsins í hverjum mánuði og ert þar af leiðandi að greiða samtals 200.000kr hvern mánuð. Til að byrja með greiðir þú reikninginn: 150.000kr og inn á lánið 50.000kr. Með tímanum mun mánaðarlega upphæðin sem bankinn rukkar lækka, en þú heldur áfram að greiða sömu upphæðina aukalega inn á höfuðstólinn. Sem dæmi væri mánaðalegur reikingurinn kominn niður í 120.000 en þú værir enn að greiða 50.000kr inn á höfuðstólinn þannig að þú værir nú að greiða í heildina 170.000kr hvern mánuð.'
    pay_adjusted_rate = 'Núna kynnum við okkur hvernig skal greiða **aðlagandi greiðslur** inn á lánið. Vinsamlegast veldu þá heildar upphæð sem að þú vilt greiða mánaðarlega þegar lagt er saman reikninginn frá bankanum og svo innborgun á lánið.'
    pay_adjusted_rate_example = 'Dæmi: Þú ert að greiða mánaðarlega 150.000kr til bankans og ert tilbúinn að verja 200.000kr í bæði að greiða þann reikning og inn á höfuðstól lánsins. Þannig að til að byrja með greiður þú reikninginn: 150.000kr og inn á lánið 50.000kr. Með tímanum mun mánaðalega upphæðin sem bankinn rukkar lækka, og þar af leiðandi getur þú aukið greiðsluna inn á höfuðstólinn. Sem dæmi væri mánaðarlegur reikningurinn kominn niður í 120.000 en þá yrðu greiðslur inn á höfuðstólinn orðnar 80.000 þar sem þú værir enn að halda áfram að greiða þessa 200.000kr mánaðarlega til húsnæðislánsins. Þannig eru greiðslunar að aðlagast breytingunum sem verða með tímanum.'
    adj_fix_difference = 'Hvað eru "aðlagandi greiðslur"?'
    extra_payment = 'Sú upphæð sem mun vera greidd aukalega inn á höfuðstól lánsins'
    extra_payment_help = ''
    monthly_extra_payment1 = 'Með því að greiða inn '
    monthly_extra_payment2 = 'munt þú ná fram eftirfarandi sparnaði'
    money_saved = 'Heildar sparnaður'
    time_saved = 'Stytting lánstíma'
    principal_downpay = 'Höfuðstóll með innborgun'
    years_and = 'ár og'
    years = 'ár'
    months = 'mánuðir'
    total_loan = "Heildar upphæð láns núna"
    loan_duration = "Lánstími eftir"
    loan_shortened_now = "Lánstími eftir núna"
    graph_title = 'Afborganir af höfuðstól lánsins'


