# Quite a messy file with the texts in Icelandic


class Text:

    # for lines
    line = "---"
    linebreak = "  "
    # The intro and header
    header = "Niðurgreiðslureiknivél fyrir íbúðalán"
    intro_text = """
    Tilgangurinn með þessari vefsíðu er að veita einstaklingum upplýsingar um hversu mikill sparnaður felst í því að greiða inn á höfuðstól láns og kosti þess að velja óverðtryggt íbúðalán framyfir verðtryggt.
    Það getur reynst bæði flókið og tímafrekt að gera svona útreikningar en þessi vefsíða er ætluð til þess að einfalda ferlið.
    Þú getur byrjað á því að velja hvernig lán þú vilt skoða og næstu skref munu sýna hvernig þú getur mögulega borgað niður lánið hraðar og sparað milljónir í vaxtagreiðslur.
    """    

    # Explain the diff between index vs non indexed loans
    index_vs_nonindex = """
    Þegar borin eru saman verðtryggð og óverðtryggð lán, koma óverðtryggð lán alltaf út sem betri kostur fyrir lántakandann.
    
    **Verðtryggð** lán fylgja verðbólgu í landinu. \
    Það þýðir að í flestum tilfellum mun skuldin hækka í hverjum mánuði um tugi eða hundruð þúsundir króna, þó að viðkomandi sé að greiða lánið mánaðarlega. 
    Það er vissulega hægt að finna nokkra mánuði síðustu áratugina þar sem verðbólgan er neikvæð og í þeim tilfellum hækkar höfuðstóll lánsins ekki, en það gerist mjög sjaldan.
    Það sem lætur verðtryggð lán líta vel út er að til að byrja með eru greiðslur á þeim lánum lægri heldur en á óverðtryggðum lánum, en það er aðeins tilfellið í nokkur ár þar sem að mánaðarlega greiðslan hækkar í hverjum mánuði og tekur fram úr mánaðarlegum greiðslum óverðtryggðra lána innan nokkurra ára.
    Á sama tíma eru greiðslur á óverðtryggðum lánum þau sömu (svo lengi sem að vextir á lánunum hækka ekki).    
    
    > **Gallar**:

    > 1. Verðtryggð lán eru látin líta út sem sá kostur sem býður lægri mánaðarlegar greiðslur fyrir fólk sem vill borga sem minnst í hverjum mánuði. 
    Raunin er sú að eftir nokkur ár verða greiðslurnar hærri og viðkomandi endar með að greiða miklu meira til baka heldur en sá sem tekur óverðtryggt lán.
    
    
    > 2. Höfuðstóll lánsins hækkar í hverjum mánuði fyrsta helming lánstímans, þannig að þú endar með að skulda hærri fjárhæð en þú fékkst lánaða.
    
    > **Kostir**:
    
    > 1. Það eru einfaldlega engir kostir sem fylgja verðtryggðum lánum. Þó að greiðslur séu vissulega lægri fyrstu árin, verða þær mikið hærri heldur en greiðslur á óverðtryggðum lánum eftir aðeins nokkur ár.

    Oft er litið á **óverðtryggð** lán sem verri kost vegna þess að til að byrja með eru afborganir á þeim lánum talsvert hærri en á sambærilegum lánum sem eru verðtryggð. 
    Hinsvegar tæki aðeins nokkur ár fyrir afborganir af verðtryggðu láni að verða jafn háar og af sambærilegu óverðtryggðu láni.
    Auk þess hækkar aldrei höfuðstóll óverðtryggða lánsins eins og gerist hjá verðtryggða láninu, sem er mikill kostur.

    
    > **Gallar**:

    > 1. Vaxtabreytingar geta haft áhrif á mánaðarlegar afborganir. 
    Núna eru vextir í sögulega lágmarki hjá Seðlabanka Íslands (0.75%) og margt sem að bendir til þess að þeir muni hækka á næstunni
    
    
    > 2. Greiðslur á þessum lánum eru háar til að byrja með, en þar sem þessi lán hækka ekki í takt við verðbólgu rétt eins og verðtryggð lán og laun flestra gera, þá mun þessi upphæð vera lægra hlutfall af tekjum einstaklings þegar lengra líður á lánstímann
    
    > **Kostir**:
    
    > 1. Þú getur sparað marga tugi milljóna í *verðbætur* sem einstaklingur sem tekur verðtryggt lán þarf að greiða

    > 2. Þú eignast fljótar hlut í eigninni þinni

    > 3. Laun hækka með tímanum samhliða verðbólgu þannig að greiðslur af láninu munu hafa minni áhrif á ráðstöfunartekjur þínar

    """

    img_non_idx_title = "Sjá dæmi um óverðtryggt lán"
    img_idx_title = "Sjá dæmi um verðtryggt lán"
    img_idx_exp_title = "Sjá dæmi um hvenær greiðslur á verðtryggðu láni verða hærri en á óverðtryggðu"
    img_non_idx_desc = "Rauði kassinn með pílunni sýnir að ekkert bætist á höfuðstól lánsins, þannig að lánið greiðist niður með tímanum"
    img_idx_desc = "Rauði kassinn með pílunni sýnir að verðbætur bætast á höfuðstól lánsins, þannig að höfuðstólinn hækkar með tímanum. Þetta er mjög slæmt fyrir þann sem tekur lánið og þekkist ekki í öðrum löndum"
    img_idx_exp_desc = "Eftir þrjú ár og fimm mánuði eru mánaðarlegar greiðslur á verðtryggðu láni orðið hærra en hjá sambærilegu óvertryggðu láni, og það mun halda áfram að hækka þar til að er greitt að fullu"


    # Step 1
    step_1 = "1. Byrjaðu á því að velja tegund láns"
    loan_type = "Tegund Láns:"
    none_selected = "Ekkert valið"
    indexed = "Verðtryggt"
    non_indexed = "Óverðtryggt"
    submit = "Staðfesta Upplýsingar"
    n_idx_diff = "Hver er munurinn á verðtryggðum og óverðtryggðum lánum?"

    # Step 2
    selected_non_indexed = "#""## Þú valdir **óverðtryggt** lán"
    selected_non_indexed_info = """
    Óverðtryggt lán er ávallt betri kosturinn þegar að það kemur að því að taka húsnæðislán.
    Til að byrja með eru mánaðarlegar greiðslur af láninu hlutfallslega hærri heldur en af sambærilegu verðtryggu láni.
    Eftir nokkur ár mun verðtryggða lánið hafa hærri greiðslur á meðan það óverðtryggða mun vera með sömu greiðslur (ef vextir breytast ekki þ.e.a.s.)
    """
    selected_indexed = "### Þú valdir **verðtryggt** lán"
    selected_indexed_info = """
    Verðtryggð lán eru ein óhagkvæmustu lán til hægt er að taka og sérstaklega til lengri tíma.
    Ef að einstaklingur er með verðtryggt lán á sinni fasteign ætti sá hin sami að **endurfjármagna lánið sitt sem fyrst** og breyta því yfir í óverðtryggt lán.
    Með okkar reiknivél getur þú séð hversu slæm þessi lán eru í raun og veru.
    """
    step_2 = "2. Fylltu út eftirfarandi reiti, ef þú ert í einhverjum vafa getur þú alltaf smellt á spurningamerkið '?' hægra meginn við reitina til þess að fá ítarlegri upplýsingar um þann reit."

    loan_amount = "Lánsupphæð"
    amount_help = """
Þetta er sú upphæð sem á eftir að greiða, hérna er hægt að setja inn lánsupphæð óháð því hvort lánið sé nýtt eða gamalt.

Dæmi: Tíu milljón króna lán skal vera fyllt inn sem '10000000' í þennan reit

+/- takkinn hækkar/lækkar um 1 milljón kr.
"""

    interest_rate = "Vextir"
    interest_rate_help = """
Vextirnir á láninu. Ef þú ert ekki viss um hverjir þeir eru getur þú nálgast þær upplýsingar í heimabankanum þínum með því að fara í lánsyfirlit.

Dæmi: Ef lánið er með 1.23% vöxtum skal setja '1.23' í þennan reit

+/- takkinn hækkar/lækkar um 1 prósentustig
"""

    inflation_rate = "Núverandi verðbólga"
    inflation_rate_help = """
Verðbólga er breytileg og getur hækkað og lækkað í framtíðinni.
Það er hægt að nálgast núverandi verðbólga á heimasíðu Seðlabanka Íslands: https://www.sedlabanki.is/ en þess má til gamans geta að verðbólgumarkmið seðlabankans er ávallt 2.5%.

Dæmi: Ef verðbólgan er 2.5% skal setja 2.5 í reitinn.

+/- takkinn hækkar/lækkar um 1 prósentustig
"""

    duration = "Lánstími eftir (í mánuðum)"
    duration_help = """
Lánstími er sá tími sem á eftir að greiða af láninu á mánuðum talið.
Það er hægt að nálgast þessa tölu í heimabankanum þínum með því að fara í lánsyfirlit.

Dæmi: Ef þú ert með lán sem hefur 25 ára lánstíma þá eru það 300 mánuðir í heildina (25 ár * 12 mánuðir í hverju ári = 300 mánuðir), þannig að í þennan reit myndir þú setja 300"

+/- takkinn hækkar/lækkar um 12 mánuði (eitt ár)
"""
    cost = "Kostnaður"
    cost_help = """
Kostnaður er mánaðarlegt gjald sem bætt er við hverja afborgun af láni (betur þekkt sem peningaplokk), upphæð fer eftir bankanum sem veitir lánið.
Þú getur nálgast þessa upphæð hjá bankanum þínum.

Arion Banki: 130kr

Landsbankinn: 120kr

Íslandsbanki: Ekki vitað
    """

    done = "Allir reitir fylltir? Smelltu hér"

    # Step 3
    step_3 = "3. Hér fyrir neðan hefur verið reiknað út hvað þú munt enda á að greiða í heildina til bankans fyrir íbúðarlánið. Í flestum tilfellum endar þú á að greiða margar milljónir í vaxtakostnað, en með því að greiða aukalega beint inn á höfuðstól lánsins er hægt að stórlækka þessa tölu. Við munum fara betur yfir það í 4. skrefi"
    wrong_input = "Settir þú inn rangar upplýsingar?"
    if_wrong_input = """
    Ef þú slóst inn einhverjar rangar upplýsingar getur þú einfaldlega lagað það í reitunum fyrir ofan til að fá út uppfærða útreikninga
    """
    # Total payments
    total_loan_payment = "Heildarkostnaður"
    total_loan_payment_info = "Þegar upp er staðið endar lántakandi oft með að greiða tugi milljóna umfram upprunalegu upphæð lánsins sem var tekið."
    total_loan_payment_help = "Hvað er heildarkostnaður?"
    total_loan_payment_desc = "Heildarkostnaður er heildarupphæðin sem er greidd fyrir lánið. Þar er lögð saman afborgun, vextir og mánaðarlegur kostnaður."
    # Interest payments
    total_interest_payment = "Vaxtagreiðslur"
    total_interest_payment_help = "Hvað eru vaxtagreiðslur?"
    total_interest_payment_desc = "Vaxtagreiðslur er heildarupphæðin sem er greidd í vexti"
    
    monthly_payments_title = "Mánaðarlegar greiðslur"
    monthly_payments_info = "Hvað eru mánaðarlegar greiðslur?"
    monthly_payments_info_desc = """
Mánaðarlegar greiðslur er sú upphæð sem að bankinn rukkar lántakanda í hverjum mánuði.
Þessi upphæð fæst með því að leggja saman afborgun, vexti, kostnað og ef lánð er verðtryggt bætast ofan á það verðbætur.
    """

    monthly_payments_desc = "Hérna er yfirlit yfir mánaðarlegar greiðslur sem þarf að greiða af láninu. Ef um óverðtryggt lán er að ræða haldast greiðslurnar nánast eins frá byrjun til enda (nema ef vextir breytast) á meðan greiðslur á verðtryggðum lánum breytast mánaðarlega og hækka hverju sinni"
    first_monthly_payments = "Fyrsta afborgun"
    last_monthly_payments = "Seinasta afborgun"
    avg_monthly_payments = "Meðaltal"

    # Interest payments
    interest_title = "Vaxtagreiðslur"
    interest_desc = """
    Vaxtagreiðslur af íbúðalánum eru oft á tíðum mjög háar og hlaupa upp í tugi milljóna fyrir hvert lán.
    Hérna er yfirlit yfir áætlaðar vaxtagreiðslur til bankans en í næsta skrefi munum við skoða hvernig hægt er að lækka þessa upphæð allverulega
    """

    stop_getting_ripped_off = "Þessir útreikningar gera ráð fyrir að þú greiðir aldrei inn á höfuðstól lánsins. Í næsta skrefi munum við kanna tvær leiðir til þess að minnka heildar vaxtagreiðslur til bankanna, en það getur verið sparnaður upp á margar milljónir."
    radio_pay_fixed_rate = "Borga fasta greiðslu inn á höfuðstól lánsins"
    radio_pay_adjusted_rate = "Borga aðlagandi greiðslu inn á höfuðstól"
    
    total_amount_with_interest = "Lán með vöxtum samtals"
    total_cost = "Samtals greiddur kostnaður"

    payment_chart = "Upphæð mánaðarlegra afborgana"
    payment_chart_desc = "Línuritið sýnir hvað mánaðarlegar afborganir eru í hverjum mánuði á verðtryggðu og óverðtryggðu íbúðaláni"


    compare_loans_title = "Samanburður á kjörum lána"
    compare_loans_title_pt2 = "lán"
    compare_loans_help = "Til hvers að gera samanburð?"
    compare_loans_info = """
Það er mikilvægt að kynna sér alla möguleika þegar kemur að því að fjárfesta í fasteign.
Svo er líka mikilvægt að sjá svart á hvítu hvor valmöguleikinn er betri kostur.
    """
    compare_loans_desc_pt1 = "Nú munum við að bera lánið saman við"
    compare_loans_desc_pt2 = "lán og skoða muninn"
    indexation = "Verðbætur"
    section = "Liður"



    # Step 4
    step_4 = "4. Hér getur þú gert áætlun um mánaðarlegar greiðslur inn á höfuðstól lánsins, en með því að borga mánaðarlega inn á höfuðstólinn getur þú sparað margar milljónir í vaxtagreiðslur og líka greitt upp lánið fyrr."
    pay_fixed_rate = "Þú hefur valið að greiða **fastar greiðslur** inn á lánið. Vinsamlegast veldu þá upphæð sem að þú vilt greiða mánaðarlega inn á lánið hérna fyrir neðan."
    pay_fixed_rate_example = "Dæmi: Þú ert að greiða mánaðarlega 150.000kr til bankans og er tilbúinn til þess að greiða ávallt 50.000kr inn á höfuðstól lánsins í hverjum mánuði og ert þar af leiðandi að greiða samtals 200.000kr hvern mánuð. Til að byrja með greiðir þú reikninginn: 150.000kr og inn á lánið 50.000kr. Með tímanum mun mánaðarlega upphæðin sem bankinn rukkar lækka, en þú heldur áfram að greiða sömu upphæðina aukalega inn á höfuðstólinn. Sem dæmi væri mánaðalegur reikingurinn kominn niður í 120.000 en þú værir enn að greiða 50.000kr inn á höfuðstólinn þannig að þú værir nú að greiða í heildina 170.000kr hvern mánuð."
    pay_adjusted_rate = "Núna kynnum við okkur hvernig greiða skuli **aðlagandi greiðslur** inn á lánið. Vinsamlegast veldu þá heildarupphæð sem að þú vilt greiða aukalega á mánuði."
    pay_adjusted_rate_example = "Dæmi: Þú ert að greiða mánaðarlega 150.000kr í afborgun af láninu og ert tilbúinn að greiða 200.000kr í heildina, s.s. afborgun plús innborgun á höfuðstól lánsins. Til að byrja með greiðir þú 150.000kr í afborgun og svo 50.000kr inn á höfuðstól lánsins. Með tímanum mun mánaðarleg afborgun lækka. Þar af leiðandi getur þú aukið greiðsluna inn á höfuðstólinn. Segjum svo að mánaðarleg afborgun sé kominn niður í 120.000kr, þá gætu greiðslur inn á höfuðstólinn verið 80.000kr, þar sem þú vilt enn að halda áfram að greiða 200.000kr mánaðarlega í heildina. Þannig eru greiðslunar að aðlagast breytingunum sem verða með tímanum."
    adj_fix_difference = 'Hvað eru aðlagandi greiðslur?'
    extra_payment = "Sú upphæð sem mun vera greidd aukalega inn á höfuðstól lánsins"
    extra_payment_help = ""
    monthly_extra_payment1 = "Með því að greiða inn "
    monthly_extra_payment2 = "munt þú ná fram eftirfarandi sparnaði"
    money_saved = "Heildarsparnaður"
    time_saved = "Stytting lánstíma"
    principal_downpay = "Höfuðstóll með innborgun"
    years_and = "ár og"
    years = "ár"
    months = "mánuðir"
    total_loan = "Heildar upphæð láns núna"
    loan_duration = "Lánstími"
    loan_shortened_now = "Lánstími eftir núna"
    graph_title = "Afborganir af láninu"
    monthy_payments = "Mánaðarlegar afborganir"

    with_payments = "Með auka greiðslu"
    without_payments = "Án auka greiðslu"
