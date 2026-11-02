"""
Domain Builder 1: Scenarios S001 to S050 (Domains 1 to 5).
Domains:
1. hr_policies (S001 - S010)
2. academic_rules (S011 - S020)
3. financial_banking (S021 - S030)
4. healthcare_medicine (S031 - S040)
5. software_cloud (S041 - S050)
"""

from scripts.scenario_definitions import DOMAINS_DATA
from scripts.scenario_data_part1 import PART1_DOMAINS

# Get Domain 1, 2, 3
D1 = PART1_DOMAINS[0]
D2 = PART1_DOMAINS[1]
D3 = PART1_DOMAINS[2]

# Domain 4: Healthcare & Medicine (S031 - S040)
D4 = {
    "domain": "healthcare_medicine",
    "scenarios": [
        {
            "topic": "Routine Blood Test Fasting Guidelines",
            "task_en": "What are the fasting guidelines prior to a comprehensive lipid panel blood test?",
            "task_hi": "लिपिड पैनल रक्त परीक्षण से पहले उपवास के दिशानिर्देश क्या हैं?",
            "task_te": "లిపిడ్ ప్రొఫైల్ రక్త పరీక్షకు ముందు పాటించవలసిన ఉపవాస నిబంధనలు ఏమిటి?",
            "task_teen": "Lipid panel blood test cheyinchukune mundu fasting guidelines emiti?",
            "doc_en": "Patients scheduled for a comprehensive fasting lipid profile or fasting blood glucose evaluation must abstain from all caloric food and beverages for 8 to 12 hours prior to venipuncture. Plain water consumption is strictly permitted and actively encouraged to ensure adequate vascular hydration during sample collection. Routine prescription medications may be taken with water unless explicitly contraindicated by the attending physician.",
            "doc_hi": "उपवास लिपिड प्रोफाइल या रक्त शर्करा परीक्षण कराने वाले मरीजों को रक्त लेने से 8 से 12 घंटे पहले सभी प्रकार के भोजन और पेय से परहेज करना चाहिए। पर्याप्त जलयोजन सुनिश्चित करने के लिए सादा पानी पीने की अनुमति है। जब तक डॉक्टर द्वारा मना न किया जाए, नियमित दवाएं पानी के साथ ली जा सकती हैं।",
            "doc_te": "లిపిడ్ ప్రొఫైల్ లేదా ఫాస్టింగ్ బ్లడ్ షుగర్ పరీక్ష చేయించుకునే రోగులు రక్త నమూనా ఇవ్వడానికి 8 నుండి 12 గంటల ముందు వరకు ఎలాంటి ఆహారం లేదా పానీయాలు తీసుకోకూడదు. శరీరంలో నీటి స్థాయిని కాపాడుకోవడానికి మంచి నీరు తాగవచ్చు. వైద్యులు ప్రత్యేకంగా వద్దని చెబితే తప్ప, రోజూ వాడే మందులను నీటితో వేసుకోవచ్చు.",
            "doc_teen": "Fasting lipid profile kani blood glucose test cheyinchukune patients blood sample ivvadaniki 8 to 12 hours mundu fasting undali. Hydration maintain cheyadaniki plain water tagavachu. Doctor specific ga apamani chepthe thappa, daily routine prescription medicines ni water tho vesukovachu."
        },
        {
            "topic": "Pediatric Vaccination Schedule",
            "task_en": "At what age should infants receive the measles, mumps, and rubella (MMR) vaccine?",
            "task_hi": "शिशुओं को खसरा, कण्ठमाला और रूबेला (एमएमआर) का टीका किस उम्र में मिलना चाहिए?",
            "task_te": "శిశువులకు మీజిల్స్, మంప్స్ మరియు రుబెల్లా (MMR) టీకాను ఏ వయస్సులో వేయించాలి?",
            "task_teen": "Infants ki MMR (measles, mumps, rubella) vaccine eppudu administer cheyali?",
            "doc_en": "The national pediatric immunization protocol recommends administering the first dose of the Measles, Mumps, and Rubella (MMR) combination vaccine between 9 and 12 months of chronological age. A secondary booster dose is administered between 15 and 18 months to ensure enduring serological protection. Minor post-vaccination reactions such as mild localized fever and transient erythema typically resolve spontaneously within 72 hours without clinical intervention.",
            "doc_hi": "राष्ट्रीय बाल टीकाकरण प्रोटोकॉल 9 से 12 महीने की उम्र के बीच खसरा, कण्ठमाला और रूबेला (एमएमआर) के पहले टीके की सिफारिश करता है। लंबे समय तक सुरक्षा सुनिश्चित करने के लिए 15 से 18 महीने के बीच एक बूस्टर खुराक दी जाती है। हल्का बुखार या लालिमा जैसी हल्की प्रतिक्रियाएं 72 घंटों के भीतर अपने आप ठीक हो जाती हैं।",
            "doc_te": "జాతీయ శిశు టీకా మార్గదర్శకాల ప్రకారం మీజిల్స్, మంప్స్ మరియు రుబెల్లా (MMR) మొదటి డోస్ టీకాను శిశువుకు 9 నుండి 12 నెలల వయస్సులో వేయించాలి. పూర్తి స్థాయి రోగనిరోధక శక్తి కోసం రెండవ బూస్టర్ డోస్‌ను 15 నుండి 18 నెలల మధ్య ఇవ్వాలి. టీకా వేసిన తర్వాత వచ్చే స్వల్ప జ్వరం లేదా దద్దుర్లు 72 గంటల్లో సహజంగానే తగ్గిపోతాయి.",
            "doc_teen": "Pediatric immunization schedule prakaram Measles, Mumps, Rubella (MMR) first dose vaccine 9 to 12 months age lo ivvali. Long-term serological protection kosam second booster dose 15 to 18 months madhyalo administer chestharu. Mild fever kani redness kani unte 72 hours lo naturally resolve avtundi."
        },
        {
            "topic": "Outpatient Appointment Rescheduling",
            "task_en": "What advance notice is required to reschedule a specialist medical consultation without penalty?",
            "task_hi": "बिना जुर्माने के विशेषज्ञ चिकित्सा परामर्श को पुनर्निर्धारित करने के लिए कितने समय पहले सूचना देनी होगी?",
            "task_te": "రుసుము లేకుండా స్పెషలిస్ట్ డాక్టర్ అపాయింట్‌మెంట్‌ను రీషెడ్యూల్ చేయడానికి ఎంత ముందుగా తెలియజేయాలి?",
            "task_teen": "Specialist medical appointment ni penalty lekunda reschedule cheyadaniki notice period enti?",
            "doc_en": "Patients seeking to cancel or reschedule a confirmed outpatient specialty consultation must notify the hospital central booking desk at least 24 hours prior to the appointment slot. Cancellations communicated with less than 24 hours notice or unattended missed appointments incur a $35 administrative clinic rebooking surcharge. Exceptions are granted solely for documented medical emergencies or acute hospitalization.",
            "doc_hi": "विशेषज्ञ परामर्श को रद्द या पुनर्निर्धारित करने के इच्छुक मरीजों को अपॉइंटमेंट से कम से कम 24 घंटे पहले अस्पताल के बुकिंग डेस्क को सूचित करना होगा। 24 घंटे से कम समय में सूचना देने या अनुपस्थित रहने पर $35 का प्रशासनिक पुनर्निर्धारण शुल्क लिया जाता है। आपात स्थिति में छूट दी जाती है।",
            "doc_te": "స్పెషలిస్ట్ డాక్టర్ కన్సల్టేషన్ అపాయింట్‌మెంట్‌ను రద్దు లేదా రీషెడ్యూల్ చేయాలనుకునే రోగులు కనీసం 24 గంటల ముందుగానే హాస్పిటల్ బుకింగ్ డెస్క్‌కు సమాచారం ఇవ్వాలి. 24 గంటల కంటే తక్కువ సమయంలో సమాచారం ఇచ్చినా లేదా రాలేకపోయినా $35 అడ్మినిస్ట్రేటివ్ రీబుకింగ్ రుసుము విధిస్తారు. తీవ్రమైన వైద్య అత్యవసర పరిస్థితుల్లో మాత్రమే దీనికి మినహాయింపు ఉంటుంది.",
            "doc_teen": "Specialist outpatient consultation cancel kani reschedule cheyali ante appointment time ki 24 hours mundu central desk ki notify cheyali. 24 hours kante thakkuva notice tho cancel chesina kani no-show ayina $35 administrative surcharge paduthundi. Medical emergencies unte matrame exemption istharu."
        },
        {
            "topic": "Prescription Refill Request Policy",
            "task_en": "How many days in advance should chronic maintenance medication refills be requested?",
            "task_hi": "पुरानी बीमारियों की दवाओं के रिफिल के लिए कितने दिन पहले अनुरोध किया जाना चाहिए?",
            "task_te": "దీర్ఘకాలిక వ్యాధుల మందుల రీఫిల్ కోసం ఎన్ని రోజుల ముందుగా దరఖాస్తు చేసుకోవాలి?",
            "task_teen": "Chronic maintenance prescription refills kosam enni days munde request pettali?",
            "doc_en": "Patients undergoing long-term therapy for chronic health conditions should submit electronic prescription refill requests at least 5 business days before exhausting their current medication supply. Specialty pharmaceutical compounds requiring prior clinical authorization or laboratory blood tier monitoring require 7 business days for processing. Emergency temporary 72-hour bridge supplies can be dispensed by the hospital pharmacy while authorization is pending.",
            "doc_hi": "पुरानी स्वास्थ्य स्थितियों के लिए दीर्घकालिक उपचार ले रहे मरीजों को दवा समाप्त होने से कम से कम 5 कार्य दिवस पहले इलेक्ट्रॉनिक रिफिल अनुरोध जमा करना चाहिए। विशेष दवाओं के लिए 7 कार्य दिवसों की आवश्यकता होती है। आपात स्थिति में 72 घंटे की दवा अस्पताल फार्मेसी द्वारा दी जा सकती है।",
            "doc_te": "దీర్ఘకాలిక వ్యాధులకు నిరంతర చికిత్స తీసుకునే రోగులు తమ వద్ద ఉన్న మందులు అయిపోవడానికి కనీసం 5 పని దినాల ముందుగానే ఈ-ప్రిస్క్రిప్షన్ రీఫిల్ అభ్యర్థనను సమర్పించాలి. ప్రత్యేక ఆమోదం అవసరమైన మందులకు 7 పని దినాల సమయం పడుతుంది. అత్యవసర సమయాల్లో ఆమోదం పెండింగ్‌లో ఉన్నప్పుడు హాస్పిటల్ ఫార్మసీ 72 గంటల తాత్కాలిక మందులను అందిస్తుంది.",
            "doc_teen": "Chronic conditions ki long-term medications teesukune patients present stock aypovadaniki 5 business days munde electronic refill request pettali. Prior authorization kavalsina specialty drugs ki 7 days processing time paduthundi. Emergency situations lo approval pending unna 72-hour bridge supply hospital pharmacy nunchi collect chesukovachu."
        },
        {
            "topic": "Hospital Inpatient Visiting Hours",
            "task_en": "What are the allowed visiting hours and visitor limits for hospital inpatient wards?",
            "task_hi": "अस्पताल के इनपेशेंट वार्डों के लिए अनुमत मिलने का समय और आगंतुक सीमाएं क्या हैं?",
            "task_te": "ఇన్‌పేషెంట్ వార్డులలో రోగులను కలవడానికి అనుమతించబడిన సమయాలు మరియు సందర్శకుల పరిమితులు ఏమిటి?",
            "task_teen": "Hospital inpatient wards lo visiting hours mariyu visitor limits emiti?",
            "doc_en": "General inpatient medical-surgical wards allow designated visitors daily between 4:00 PM and 7:00 PM. To maintain infection control standards and ensure patient rest, a maximum of 2 visitors are permitted at the patient bedside at any given time. All visitors must undergo thermal screening and sanitize their hands at the ward nursing station. Children under the age of 12 are prohibited from inpatient wards except under compassionate end-of-life care allowances.",
            "doc_hi": "सामान्य इनपेशेंट वार्डों में प्रतिदिन शाम 4:00 बजे से 7:00 बजे के बीच आगंतुकों को अनुमति दी जाती है। संक्रमण नियंत्रण बनाए रखने के लिए, एक समय में अधिकतम 2 आगंतुकों को मरीज के पास जाने की अनुमति है। सभी आगंतुकों को वार्ड में हाथ साफ करना अनिवार्य है। 12 वर्ष से कम उम्र के बच्चों का प्रवेश प्रतिबंधित है।",
            "doc_te": "జనరల్ ఇన్ పేషెంట్ వార్డులలో చికిత్స పొందుతున్న రోగులను చూడటానికి ప్రతిరోజూ సాయంత్రం 4:00 నుండి 7:00 గంటల వరకు మాత్రమే అనుమతిస్తారు. ఇన్‌ఫెక్షన్ నియంత్రణ మరియు రోగి విశ్రాంతి కోసం ఒకే సమయంలో గరిష్టంగా ఇద్దరు సందర్శకులను మాత్రమే బెడ్ దగ్గరకు అనుమతిస్తారు. వార్డులోకి ప్రవేశించే ముందు శానిటైజర్ వాడటం తప్పనిసరి. 12 సంవత్సరాల లోపు పిల్లలను వార్డులలోకి అనుమతించరు.",
            "doc_teen": "General inpatient wards lo daily evening 4:00 PM nunchi 7:00 PM varaku visiting hours untayi. Infection control mariyu patient rest kosam bedside daggara at a time maximum 2 visitors matrame allow chestharu. Ward loki velletappudu thermal screening mariyu hand sanitization compulsory. 12 years lopala unna children ki inpatient wards lo entry undadhu."
        },
        {
            "topic": "Medical Records Disclosure Protocol",
            "task_en": "How quickly must the hospital release copies of certified medical records following a patient request?",
            "task_hi": "मरीज के अनुरोध के बाद अस्पताल को कितनी जल्दी प्रमाणित मेडिकल रिकॉर्ड की प्रतियां जारी करनी होंगी?",
            "task_te": "రోగి అభ్యర్థించిన తర్వాత ఎన్ని రోజుల్లోగా ఆసుపత్రి ధృవీకరించిన వైద్య రికార్డులను విడుదల చేయాలి?",
            "task_teen": "Patient request chesina tharuvatha certified medical records release cheyadaniki time entha?",
            "doc_en": "In compliance with health data privacy and patient access laws, hospital health information departments must fulfill verified patient requests for certified medical records within 7 business days of receiving written authorization. Records may be delivered securely via the encrypted patient web portal or as sealed physical copies upon presentation of photographic identification. A standard administrative reproduction fee of $15 applies to paper printouts exceeding 25 pages.",
            "doc_hi": "स्वास्थ्य डेटा गोपनीयता नियमों के अनुसार, अस्पताल को लिखित प्राधिकरण प्राप्त होने के 7 कार्य दिवसों के भीतर प्रमाणित मेडिकल रिकॉर्ड जारी करने होंगे। रिकॉर्ड मरीज पोर्टल के माध्यम से या फोटो पहचान प्रस्तुत करने पर भौतिक रूप से दिए जा सकते हैं। 25 से अधिक पृष्ठों के प्रिंटआउट पर $15 का शुल्क लागू होता है।",
            "doc_te": "హెల్త్ డేటా గోప్యతా చట్టాల ప్రకారం, రోగి లిఖితపూర్వక అభ్యర్థన సమర్పించిన 7 పని దినాల్లోగా ఆసుపత్రి ధృవీకరించిన మెడికల్ రికార్డులను విడుదల చేయాలి. రికార్డులను రోగి వెబ్ పోర్టల్ ద్వారా ఎన్‌క్రిప్టెడ్ రూపంలో లేదా ఫోటో ఐడీ చూపించి భౌతిక కాపీలుగా తీసుకోవచ్చు. 25 పేజీలకు మించిన పేపర్ ప్రింట్‌అవుట్లకు $15 ప్రామాణిక పరిపాలనా రుసుము వసూలు చేస్తారు.",
            "doc_teen": "Health data privacy guidelines prakaram written authorization receive ayina 7 business days lopala certified medical records release cheyali. Encrypted patient web portal dwara kani photo ID chupinchi physical copies kani teesukovachu. 25 pages kante ekkuva paper copies unte $15 administrative reproduction fee paduthundi."
        },
        {
            "topic": "Emergency Room Triage Tiers",
            "task_en": "Explain the 5-level Emergency Severity Index (ESI) used for hospital triage prioritization.",
            "task_hi": "अस्पताल में आपातकालीन प्राथमिकता के लिए उपयोग किए जाने वाले 5-स्तरीय ईएसआई (ESI) को समझाएं।",
            "task_te": "ఆసుపత్రి ఎమర్జెన్సీ వార్డులో రోగుల ప్రాధాన్యతను నిర్ణయించే 5-స్థాయిల ESI విధానాన్ని వివరించండి.",
            "task_teen": "Hospital triage prioritization lo use chese 5-level Emergency Severity Index (ESI) explain cheyandi.",
            "doc_en": "Emergency departments utilize the standardized 5-tier Emergency Severity Index (ESI) to triage incoming patients. Level 1 denotes Resuscitation requiring immediate life-saving intervention; Level 2 indicates Emergent conditions with high risk of deterioration; Level 3 signifies Urgent presentations requiring multiple diagnostic modalities; Level 4 represents Less Urgent cases needing a single diagnostic test; and Level 5 represents Non-Urgent clinical presentations treatable with routine outpatient care.",
            "doc_hi": "आपातकालीन विभाग मरीजों की प्राथमिकता तय करने के लिए 5-स्तरीय आपातकालीन गंभीरता सूचकांक (ESI) का उपयोग करते हैं। स्तर 1 तत्काल जीवन रक्षक हस्तक्षेप है; स्तर 2 उच्च जोखिम वाली आपातकालीन स्थिति है; स्तर 3 गंभीर मामले हैं जिनमें कई परीक्षणों की आवश्यकता होती है; स्तर 4 कम जरूरी मामले हैं; और स्तर 5 गैर-जरूरी मामले हैं जिनका सामान्य इलाज संभव है।",
            "doc_te": "ఎమర్జెన్సీ విభాగంలో రోగుల ప్రాధాన్యతను నిర్ణయించడానికి 5-స్థాయిల ఎమర్జెన్సీ సివియారిటీ ఇండెక్స్ (ESI) విధానాన్ని ఉపయోగిస్తారు. లెవల్ 1 తక్షణ ప్రాణ రక్షణ అవసరమైన అత్యవసర పరిస్థితి; లెవల్ 2 తీవ్రమైన సమస్యలు; లెవల్ 3 తక్షణ పరీక్షలు అవసరమైన కేసులు; లెవల్ 4 ఒకే పరీక్ష అవసరమైన తక్కువ అత్యవసర కేసులు; మరియు లెవల్ 5 సాధారణ ఔట్ పేషెంట్ సంరక్షణతో నయమయ్యే సాధారణ కేసులు.",
            "doc_teen": "Emergency triage lo 5-tier Emergency Severity Index (ESI) follow avtharu: Level 1 ante immediate life-saving resuscitation; Level 2 high-risk emergent condition; Level 3 multiple diagnostic tests kavalsina urgent case; Level 4 single test kavalsina less urgent presentation; Level 5 routine care tho treat cheyagalige non-urgent issue."
        },
        {
            "topic": "Diabetic Meal Carbohydrate Guidelines",
            "task_en": "What is the recommended dietary carbohydrate intake per meal for diabetic management?",
            "task_hi": "मधुमेह प्रबंधन के लिए प्रति भोजन अनुशंसित आहार कार्बोहाइड्रेट की मात्रा क्या है?",
            "task_te": "మధుమేహ నియంత్రణ కోసం ప్రతి భోజనంలో సిఫార్సు చేయబడిన కార్బోహైడ్రేట్ల పరిమాణం ఎంత?",
            "task_teen": "Diabetes management lo prathi meal ki recommended carbohydrate intake entha undali?",
            "doc_en": "Clinical nutrition guidelines for adult type 2 diabetes management recommend consuming between 45 and 60 grams of complex carbohydrates per main meal. Patients should prioritize unrefined, high-fiber carbohydrate sources such as whole grains, legumes, and non-starchy vegetables while avoiding simple sugars and high-glycemic sweetened beverages. Maintaining regular meal spacing every 4 to 5 hours helps stabilize postprandial glycemic excursions.",
            "doc_hi": "टाइप 2 मधुमेह प्रबंधन के लिए पोषण संबंधी दिशानिर्देश प्रति मुख्य भोजन में 45 से 60 ग्राम जटिल कार्बोहाइड्रेट का उपभोग करने की सलाह देते हैं। मरीजों को साबुत अनाज, फलियां और हरी सब्जियों जैसे उच्च फाइबर वाले स्रोतों को प्राथमिकता देनी चाहिए और मीठे पेय पदार्थों से बचना चाहिए। हर 4 से 5 घंटे में भोजन करने से रक्त शर्करा स्थिर रहती है।",
            "doc_te": "టైప్ 2 మధుమేహ నియంత్రణ మార్గదర్శకాల ప్రకారం ప్రతి ప్రధాన భోజనంలో 45 నుండి 60 గ్రాముల కాంప్లెక్స్ కార్బోహైడ్రేట్లను తీసుకోవాలని సిఫార్సు చేస్తున్నారు. రోగులు తృణధాన్యాలు, పప్పుధాన్యాలు మరియు పీచు పదార్థాలు ఎక్కువగా ఉండే కూరగాయలను ఎంచుకోవాలి మరియు తీపి పదార్థాలు, చక్కెర పానీయాలను పూర్తిగా నివారించాలి. ప్రతి 4 నుండి 5 గంటలకు భోజనం చేయడం వల్ల రక్తంలో చక్కెర స్థాయిలు అదుపులో ఉంటాయి.",
            "doc_teen": "Type 2 diabetes management nutrition guidelines prakaram prathi meal lo 45 to 60 grams complex carbohydrates teesukovali. Whole grains, legumes mariyu leafy vegetables lanti high-fiber sources ki priority ivvali, refined sugars ni avoid cheyali. Regular ga 4 to 5 hours gap lo meals plan chesthe postprandial blood sugar spikes control avtayi."
        },
        {
            "topic": "Post-Operative Wound Care Protocol",
            "task_en": "How should surgical wound dressings be managed during the first 48 hours following surgery?",
            "task_hi": "सर्जरी के बाद पहले 48 घंटों के दौरान सर्जिकल घाव की ड्रेसिंग का प्रबंधन कैसे किया जाना चाहिए?",
            "task_te": "శస్త్రచికిత్స జరిగిన మొదటి 48 గంటల్లో గాయానికి వేసిన డ్రెస్సింగ్‌ను ఎలా సంరక్షించాలి?",
            "task_teen": "Surgery tharuvatha first 48 hours surgical wound dressing ni ela care teesukovali?",
            "doc_en": "Following elective surgical procedures, sterile surgical dressings must remain completely dry and undisturbed for the initial 48 hours post-discharge. Patients should inspect the outer dressing twice daily for signs of abnormal serosanguinous drainage, foul odor, or localized warmth. Routine sponge bathing is permissible, but direct immersion in baths, swimming pools, or hot showers is contraindicated until initial suture or staple removal at the post-op follow-up.",
            "doc_hi": "सर्जरी के बाद प्राथमिक 48 घंटों के लिए सर्जिकल ड्रेसिंग को पूरी तरह से सूखा और सुरक्षित रखा जाना चाहिए। मरीजों को असामान्य रिसाव, दुर्गंध या गर्माहट के संकेतों के लिए दिन में दो बार बाहरी पट्टी का निरीक्षण करना चाहिए। स्पंज से नहाना अनुमत है, लेकिन टांके हटने तक टब में नहाने या तैरने से बचना चाहिए।",
            "doc_te": "శస్త్రచికిత్స పూర్తయిన తర్వాత మొదటి 48 గంటల పాటు సర్జికల్ డ్రెస్సింగ్‌ను పూర్తిగా పొడిగా మరియు కదల్చకుండా ఉంచాలి. రక్తస్రావం, దుర్వాసన లేదా వాపు వంటి లక్షణాలు ఉన్నాయేమో రోగులు రోజుకు రెండుసార్లు డ్రెస్సింగ్‌ను పరిశీలించాలి. స్పాంజ్ బాత్ చేయవచ్చు కానీ కుట్లు విప్పే వరకు షవర్ కింద నేరుగా స్నానం చేయడం లేదా స్విమ్మింగ్ పూల్‌లోకి వెళ్లడం ఖచ్చితంగా నిషిద్ధం.",
            "doc_teen": "Surgery tharuvatha sterile surgical dressing ni initial 48 hours completely dry ga maintain cheyali, disturb cheyakudadhu. Abnormal discharge, bad smell kani swelling unte notice cheyali. Sponge bath chesukovachu kani sutures kani staples remove chese varaku direct hot shower kani swimming pools lo bath cheyadam allow cheyaru."
        },
        {
            "topic": "Elective Surgery Health Insurance Pre-Authorization",
            "task_en": "What is the advance submission deadline for insurance pre-authorization of elective surgery?",
            "task_hi": "वैकल्पिक सर्जरी के बीमा पूर्व-प्राधिकरण के लिए अग्रिम प्रस्तुत करने की समय सीमा क्या है?",
            "task_te": "ఎలెక్టివ్ సర్జరీ కోసం హెల్త్ ఇన్సూరెన్స్ ప్రీ-ఆథరైజేషన్ ఎన్ని గంటల ముందు సమర్పించాలి?",
            "task_teen": "Elective surgery health insurance pre-authorization enni hours munde submit cheyali?",
            "doc_en": "Inpatient elective surgical procedures covered by commercial health insurance require prior clinical authorization submitted at least 72 hours prior to hospital admission. The treating hospital must transmit comprehensive diagnostic imaging reports, attending surgeon clinical notes, and itemized billing estimates to the insurer's medical review committee. Emergency life-saving procedures are exempt from pre-authorization provided notification is filed within 24 hours of admission.",
            "doc_hi": "स्वास्थ्य बीमा द्वारा कवर की जाने वाली वैकल्पिक सर्जरी के लिए अस्पताल में भर्ती होने से कम से कम 72 घंटे पहले पूर्व-प्राधिकरण जमा करना आवश्यक है। अस्पताल को बीमाकर्ता को नैदानिक रिपोर्ट और बिलिंग अनुमान भेजना होगा। आपातकालीन जीवन रक्षक प्रक्रियाओं को छूट दी गई है, बशर्ते 24 घंटे के भीतर सूचना दी जाए।",
            "doc_te": "హెల్త్ ఇన్సూరెన్స్ వర్తించే ఎలెక్టివ్ సర్జరీలకు ఆసుపత్రిలో చేరడానికి కనీసం 72 గంటల ముందుగానే ప్రీ-ఆథరైజేషన్ దరఖాస్తును సమర్పించాలి. ఆసుపత్రి యాజమాన్యం అవసరమైన స్కానింగ్ నివేదికలు, సర్జన్ నోట్స్ మరియు అంచనా బిల్లు వివరాలను బీమా సంస్థకు పంపాలి. ప్రాణాపాయ అత్యవసర శస్త్రచికిత్సలకు ఈ ముందస్తు అనుమతి అవసరం లేదు, చేరిన 24 గంటల్లో సమాచారం ఇస్తే సరిపోతుంది.",
            "doc_teen": "Elective inpatient surgeries ki health insurance pre-authorization hospital admission ki at least 72 hours mundu submit cheyali. Diagnostic imaging reports, surgeon clinical notes mariyu billing estimates insurance review team ki pampali. Emergency life-saving cases lo admission ayina 24 hours lo claim initiate chesthe pre-authorization exemption untundi."
        }
    ]
}

# Domain 5: Software & Cloud Infrastructure (S041 - S050)
D5 = {
    "domain": "software_cloud",
    "scenarios": [
        {
            "topic": "Kubernetes Horizontal Pod Autoscaler",
            "task_en": "What is the default CPU utilization target that triggers horizontal pod autoscaling?",
            "task_hi": "हॉरिजॉन्टल पॉड ऑटोस्केलिंग को ट्रिगर करने वाला डिफ़ॉल्ट CPU उपयोग लक्ष्य क्या है?",
            "task_te": "కుబెర్‌నెటీస్‌లో క్లస్టర్ పాడ్స్ ఆటోస్కేలింగ్‌ను ట్రిగ్గర్ చేసే డిఫాల్ట్ CPU పరిమితి ఎంత?",
            "task_teen": "Kubernetes Horizontal Pod Autoscaler (HPA) scale avvadaniki default CPU target entha?",
            "doc_en": "In production Kubernetes clusters, the Horizontal Pod Autoscaler (HPA) controller monitors target workload metrics and adjusts pod replica counts automatically. By standard deployment convention, the target average CPU utilization threshold is configured at 75% of container resource requests. When average CPU exceeds this threshold across a continuous 3-minute stabilization window, HPA scales up replicas up to the configured maximum cluster limit.",
            "doc_hi": "उत्पादन कुबेरनेट्स क्लस्टर में, हॉरिज़ॉन्टल पॉड ऑटोस्केलर (एचपीए) कंटेनर रिसोर्स अनुरोधों के 75% के डिफ़ॉल्ट औसत सीपीयू उपयोग पर काम करता है। जब लगातार 3 मिनट की अवधि में औसत सीपीयू इस सीमा से अधिक हो जाता है, तो एचपीए स्वचालित रूप से पॉड प्रतियों की संख्या को अधिकतम सीमा तक बढ़ा देता है।",
            "doc_te": "ప్రొడక్షన్ కుబెర్‌నెటీస్ క్లస్టర్లలో, హారిజాంటల్ పాడ్ ఆటోస్కేలర్ (HPA) కంటైనర్ వనరుల వినియోగాన్ని పర్యవేక్షిస్తుంది. సాధారణ ప్రమాణాల ప్రకారం, సగటు CPU వినియోగ పరిమితిని 75% వద్ద కాన్ఫిగర్ చేస్తారు. వరుసగా 3 నిమిషాల వ్యవధిలో CPU వినియోగం 75% దాటితే, HPA స్వయంచాలకంగా పాడ్స్ సంఖ్యను గరిష్ట పరిమితి వరకు పెంచుతుంది (స్కేల్ అప్).",
            "doc_teen": "Production Kubernetes clusters lo Horizontal Pod Autoscaler (HPA) pod replicas ni dynamically adjust chesthundi. Standard deployment lo default target CPU utilization 75% configure chestharu. Continuous 3-minute stabilization window lo average CPU 75% exceed ayithe HPA replicas ni max cluster limit varaku scale up chesthundi."
        },
        {
            "topic": "Docker Container Non-Root User Best Practice",
            "task_en": "Why should Docker containers run as non-root users in production environments?",
            "task_hi": "उत्पादन परिवेश में डॉकर कंटेनरों को गैर-रूट उपयोगकर्ताओं के रूप में क्यों चलना चाहिए?",
            "task_te": "ప్రొడక్షన్ వాతావరణంలో డాకర్ కంటైనర్లను నాన్-రూట్ యూజర్‌గా ఎందుకు రన్ చేయాలి?",
            "task_teen": "Production lo Docker containers ni non-root user tho enduku run cheyali?",
            "doc_en": "Enterprise container hardening policies require production Docker container images to execute application processes under an explicitly declared unprivileged non-root user (e.g., UID 10001). Running containers as the default root user poses severe container escape risks: if an attacker achieves arbitrary code execution within the container, they inherit root-level kernel capabilities on the underlying Linux host OS.",
            "doc_hi": "एंटरप्राइज़ सुरक्षा नीतियों के तहत डॉकर कंटेनरों को एक गैर-रूट उपयोगकर्ता (जैसे यूआईडी 10001) के तहत चलाना आवश्यक है। डिफ़ॉल्ट रूट उपयोगकर्ता के रूप में कंटेनर चलाने से सुरक्षा जोखिम पैदा होता है: यदि कोई कंटेनर में सेंध लगाता है, तो उसे अंतर्निहित होस्ट ओएस पर रूट-स्तरीय अधिकार मिल जाते हैं।",
            "doc_te": "ఎంటర్‌ప్రైజ్ సెక్యూరిటీ నిబంధనల ప్రకారం ప్రొడక్షన్ డాకర్ కంటైనర్లను ప్రత్యేకంగా నాన్-రూట్ యూజర్ (ఉదాహరణకు UID 10001) కింద మాత్రమే రన్ చేయాలి. డెవలపర్లు డిఫాల్ట్ రూట్ యూజర్‌గా రన్ చేస్తే కంటైనర్ ఎస్కేప్ ప్రమాదాలు ఏర్పడతాయి: కంటైనర్‌లో కోడ్ ఎగ్జిక్యూషన్ లోపం జరిగితే హ్యాకర్లకు హోస్ట్ ఆపరేటింగ్ సిస్టమ్‌పై కూడా రూట్ ప్రివిలేజ్‌లు లభించే ప్రమాదం ఉంది.",
            "doc_teen": "Container security hardening lo production Docker images ni non-root unprivileged user (UID 10001) kindha run cheyadam mandatory. Containers ni default root ga run chesthe container escape risk ekkuva: attacker container compromise chesthe underlying host Linux OS pai kuda root kernel capabilities gain chese scope untundi."
        },
        {
            "topic": "PostgreSQL Connection Pooling Configurations",
            "task_en": "What is the recommended PgBouncer connection pool size per CPU core for PostgreSQL?",
            "task_hi": "PostgreSQL के लिए प्रति CPU कोर अनुशंसित PgBouncer कनेक्शन पूल आकार क्या है?",
            "task_te": "PostgreSQL కోసం ప్రతి CPU కోర్‌కు సిఫార్సు చేయబడిన PgBouncer కనెక్షన్ పూల్ సైజు ఎంత?",
            "task_teen": "PostgreSQL database kosam per CPU core PgBouncer connection pool size entha undali?",
            "doc_en": "PostgreSQL utilizes a process-per-connection architecture where excessive client connections generate significant CPU context switching overhead. Best practices dictate deploying PgBouncer in transaction pooling mode, configuring the pool size using the formula: (CPU Cores * 2) + Disk Spindles, typically yielding 15 to 20 active connections per core. Client applications reuse these persistent backend slots, avoiding fork latency.",
            "doc_hi": "PostgreSQL एक प्रोसेस-प्रति-कनेक्शन आर्किटेक्चर का उपयोग करता है जहां अत्यधिक कनेक्शन सीपीयू पर दबाव डालते हैं। सर्वोत्तम प्रथाओं के अनुसार PgBouncer को ट्रांजेक्शन पूलिंग मोड में तैनात किया जाता है, जिसमें प्रति कोर 15 से 20 सक्रिय कनेक्शन का आकार रखा जाता है। इससे सर्वर पर ओवरहेड कम होता है।",
            "doc_te": "PostgreSQL డేటాబేస్ ప్రతి కనెక్షన్‌కు ఒక ప్రాసెస్‌ను ఉపయోగిస్తుంది, దీనివల్ల ఎక్కువ కనెక్షన్లు ఉన్నప్పుడు CPU పై తీవ్ర ఒత్తిడి పడుతుంది. ఉత్తమ పనితీరు కోసం PgBouncer ని ట్రాన్సాక్షన్ పూలింగ్ మోడ్‌లో కాన్ఫిగర్ చేసి, ప్రతి CPU కోర్‌కు 15 నుండి 20 కనెక్షన్లు ఉండేలా చూడాలి. దీనివల్ల అప్లికేషన్లు ఇప్పటికే ఉన్న బ్యాకెండ్ కనెక్షన్లను తిరిగి వాడుకుని వేగంగా పనిచేస్తాయి.",
            "doc_teen": "PostgreSQL process-per-connection architecture use chesthundi kabatti excessive connections unte CPU context switching overhead peruguthundi. PgBouncer ni transaction pooling mode lo deploy chesi, core ki 15 to 20 active connections pool size configure cheyadam best practice. Deeni valla fork latency lekunda reusable persistent connections access avtayi."
        },
        {
            "topic": "AWS S3 Glacier Lifecycle Transition Rules",
            "task_en": "After how many days do S3 lifecycle rules transition objects to Glacier Flexible Archive?",
            "task_hi": "S3 लाइफ़साइकिल नियम कितने दिनों के बाद ऑब्जेक्ट्स को ग्लेशियर फ्लेक्सिबल आर्काइव में स्थानांतरित करते हैं?",
            "task_te": "AWS S3 లైఫ్‌సైకిల్ నియమాలు ఎన్ని రోజుల తర్వాత ఫైళ్లను గ్లేసియర్ ఆర్కైవ్‌కు బదిలీ చేస్తాయి?",
            "task_teen": "AWS S3 lifecycle transition rules lo objects ni Glacier Flexible Archive ki enni days lo move chestharu?",
            "doc_en": "Amazon S3 lifecycle management rules automate tiered storage cost optimization. Standard corporate archival policies specify that infrequently accessed log files and database dumps transition from S3 Standard to S3 Standard-Infrequent Access at 30 days, followed by automatic transition to S3 Glacier Flexible Archive at 90 days. Objects retained past 365 days undergo permanent automated purge deletion.",
            "doc_hi": "अमेज़ॅन S3 लाइफ़साइकिल नियम स्टोरेज लागत को अनुकूलित करते हैं। मानक कॉर्पोरेट नीतियों के अनुसार, फ़ाइलें 30 दिनों में S3 स्टैंडर्ड से S3 इन्फ्रीक्वेंट एक्सेस में और 90 दिनों में स्वचालित रूप से S3 ग्लेशियर फ्लेक्सिबल आर्काइव में स्थानांतरित हो जाती हैं। 365 दिनों के बाद वस्तुएं स्थायी रूप से हटा दी जाती हैं।",
            "doc_te": "Amazon S3 లైఫ్‌సైకిల్ నిర్వహణ విధానం స్టోరేజ్ ఖర్చులను ఆదా చేస్తుంది. సాధారణ నిబంధనల ప్రకారం, తరచుగా ఉపయోగించని లాగ్ ఫైళ్లు 30 రోజుల తర్వాత S3 Standard-IA కి మారతాయి మరియు 90 రోజుల తర్వాత స్వయంచాలకంగా S3 Glacier Flexible Archive కి బదిలీ చేయబడతాయి. 365 రోజులు పూర్తయిన తర్వాత ఆ ఫైళ్లు శాశ్వతంగా తొలగించబడతాయి.",
            "doc_teen": "Amazon S3 lifecycle management storage cost optimization ni automate chesthundi. Standard archival policies prakaram logs mariyu backups 30 days lo S3 Standard-IA ki move avtayi, mariyu 90 days complete avvagane automatic ga S3 Glacier Flexible Archive ki transition avtayi. 365 days taruvatha permanent purge deletion jarugutundi."
        },
        {
            "topic": "Redis Cache Eviction Strategy",
            "task_en": "How does the volatile-lru eviction policy function when Redis memory is exhausted?",
            "task_hi": "जब रेडिस मेमोरी समाप्त हो जाती है तो volatile-lru निष्कासन नीति कैसे काम करती है?",
            "task_te": "రెడిస్ మెమరీ నిండిపోయినప్పుడు volatile-lru పాలసీ ఎలా పనిచేస్తుంది?",
            "task_teen": "Redis memory limit reach ayinappudu volatile-lru eviction policy ela behave chesthundi?",
            "doc_en": "When a Redis caching instance reaches its configured maxmemory threshold, it triggers its eviction algorithm to reclaim RAM. Under the 'volatile-lru' (Least Recently Used) policy, Redis inspects only the subset of keys that have an explicit time-to-live (TTL) expiration set, evicting the keys accessed least recently. Persistent keys lacking an expiration timer are preserved indefinitely without risk of automated eviction.",
            "doc_hi": "जब रेडिस अपनी अधिकतम मेमोरी सीमा तक पहुँच जाता है, तो यह खाली जगह बनाने के लिए निष्कासन शुरू करता है। 'volatile-lru' नीति के तहत, रेडिस केवल उन कुंजियों को हटाता है जिनका एक निश्चित समाप्ति समय (TTL) होता है और जो हाल ही में सबसे कम उपयोग की गई हों। बिना समाप्ति वाली कुंजियां सुरक्षित रहती हैं।",
            "doc_te": "రెడిస్ క్యాషింగ్ సర్వర్ తన గరిష్ట మెమరీ పరిమితికి చేరుకున్నప్పుడు, మెమరీని ఖాళీ చేయడానికి ఎవిక్షన్ పద్ధతిని ప్రారంభిస్తుంది. 'volatile-lru' పాలసీ కింద, రెడిస్ కేవలం గడువు సమయం (TTL) నిర్ణయించబడిన కీలలో అత్యంత తక్కువగా వాడిన (Least Recently Used) కీలను మాత్రమే తొలగిస్తుంది. గడువు లేని శాశ్వత కీలు డిలీట్ కాకుండా సురక్షితంగా ఉంటాయి.",
            "doc_teen": "Redis maxmemory threshold reach ayinappudu RAM reclaim cheyadaniki eviction algorithm trigger avtundi. 'volatile-lru' policy lo explicit TTL expiration unna keys lo least recently used keys ni matrame evict chesthundi. Expiration timer leni persistent keys safe ga untayi, avi delete avvavu."
        },
        {
            "topic": "CI/CD Code Coverage Quality Gates",
            "task_en": "What minimum code coverage percentage must a pull request achieve to pass the CI gate?",
            "task_hi": "सीआई गेट पास करने के लिए पुल अनुरोध में न्यूनतम कितना कोड कवरेज प्रतिशत होना चाहिए?",
            "task_te": "CI/CD పైప్‌లైన్‌లో కోడ్ కవరేజ్ గేట్ పాస్ కావడానికి కనీస శాతం ఎంత ఉండాలి?",
            "task_teen": "Pull request merge avvali ante CI pipeline lo minimum code coverage gate percentage entha?",
            "doc_en": "Engineering development standards enforce automated SonarQube quality gates on all CI/CD integration pipelines. Pull requests targeting the release branch must demonstrate a minimum of 80% line test coverage on newly added code, zero critical security vulnerability findings, and less than 3% technical debt duplication. Pull requests failing these thresholds are blocked from merging into upstream repositories.",
            "doc_hi": "इंजीनियरिंग मानकों के अनुसार सभी सीआई/सीडी पाइपलाइनों पर 80% कोड कवरेज की आवश्यकता होती है। नई जोड़ी गई कोड लाइनों पर 80% टेस्ट कवरेज होना चाहिए और कोई सुरक्षा भेद्यता नहीं होनी चाहिए। इन मानकों को पूरा न करने वाले पुल अनुरोधों को मुख्य शाखा में विलय करने से रोक दिया जाता है।",
            "doc_te": "సాఫ్ట్‌వేర్ ఇంజనీరింగ్ ప్రమాణాల ప్రకారం CI/CD పైప్‌లైన్‌లలో SonarQube క్వాలిటీ గేట్లు ఉంటాయి. మెయిన్ బ్రాంచ్‌లో మెర్జ్ కావాలంటే కొత్తగా రాసిన కోడ్‌లో కనీసం 80% లైన్ టెస్ట్ కవరేజ్ ఉండాలి, ఎటువంటి తీవ్రమైన సెక్యూరిటీ లోపాలు ఉండకూడదు మరియు డూప్లికేషన్ 3% కంటే తక్కువ ఉండాలి. ఈ పరిమితులను సాధించని పుల్ రిక్వెస్ట్‌లను బ్లాక్ చేస్తారు.",
            "doc_teen": "CI/CD integration pipelines lo SonarQube quality gates mandatory ga check chesthayi. Release branch ki merge chese pull requests lo newly added code ki minimum 80% test coverage undali, critical security vulnerabilities undakudadhu mariyu 3% kante thakkuva duplication undali. Idi fail ayithe PR merge block avtundi."
        },
        {
            "topic": "OAuth 2.0 JWT Token Lifetimes",
            "task_en": "What are the standard expiration durations for OAuth 2.0 access and refresh tokens?",
            "task_hi": "OAuth 2.0 एक्सेस और रिफ्रेश टोकन के लिए मानक समाप्ति अवधि क्या हैं?",
            "task_te": "OAuth 2.0 లో యాక్సెస్ మరియు రీఫ్రెష్ టోకెన్ల ప్రామాణిక గడువు సమయం ఎంత?",
            "task_teen": "OAuth 2.0 JWT access token mariyu refresh token standard expiration lifetimes enti?",
            "doc_en": "Corporate microservice identity architecture enforces short-lived OAuth 2.0 JSON Web Tokens (JWT) for API authorization. Bearer access tokens carry a strict 15-minute expiration lifespan to mitigate token hijacking exposure. Long-lived refresh tokens possess a 7-day validity duration and are stored in cryptographically secured HTTP-only cookies equipped with automated token rotation upon each exchange.",
            "doc_hi": "कॉर्पोरेट सुरक्षा के लिए OAuth 2.0 में एक्सेस टोकन 15 मिनट की सख्त समाप्ति अवधि के साथ आते हैं ताकि टोकन चोरी के जोखिम को कम किया जा सके। रिफ्रेश टोकन 7 दिनों के लिए मान्य होते हैं और प्रत्येक उपयोग पर स्वचालित रूप से बदल दिए जाते हैं।",
            "doc_te": "కార్పొరేట్ మైక్రోసర్వీస్ ఆర్కిటెక్చర్‌లో API యాక్సెస్ కొరకు స్వల్పకాలిక OAuth 2.0 JWT టోకెన్లను ఉపయోగిస్తారు. టోకెన్ హైజాకింగ్ ప్రమాదాన్ని అరికట్టడానికి యాక్సెస్ టోకెన్లకు కేవలం 15 నిమిషాల గడువు మాత్రమే ఉంటుంది. రీఫ్రెష్ టోకెన్లు 7 రోజుల పాటు చెల్లుబాటు అవుతాయి మరియు ప్రతిసారీ ఆటోమేటిక్ రొటేషన్ పద్ధతిలో పనిచేస్తాయి.",
            "doc_teen": "OAuth 2.0 identity architecture lo security kosam short-lived JWT access tokens use chestharu. Bearer access tokens ki strict ga 15 minutes expiration untundi to prevent token theft. Refresh tokens 7 days validity tho untayi mariyu cryptographically secured HTTP-only cookies lo save chesi prathi usage ki rotate chestharu."
        },
        {
            "topic": "Microservice Circuit Breaker Failure Thresholds",
            "task_en": "When does a microservice circuit breaker transition to the open state?",
            "task_hi": "माइक्रोसर्विस सर्किट ब्रेकर कब ओपन स्थिति में बदल जाता है?",
            "task_te": "మైక్రోసర్వీస్ ఆర్కిటెక్చర్‌లో సర్క్యూట్ బ్రేకర్ ఎప్పుడు ఓపెన్ స్టేట్‌కు మారుతుంది?",
            "task_teen": "Microservice circuit breaker eppudu open state loki transition avtundi?",
            "doc_en": "Distributed resilience patterns implement circuit breakers (via Envoy or Resilience4j) to prevent cascading microservice outages. A circuit breaker monitors downstream dependency calls over a rolling 10-second window. If consecutive HTTP 5xx failures or response timeouts exceed 5 failures or a 50% error rate, the circuit transitions to the 'Open' state, instantly failing-fast without forwarding requests to the failing backend.",
            "doc_hi": "माइक्रोसर्विस में विफलता को फैलने से रोकने के लिए सर्किट ब्रेकर का उपयोग किया जाता है। यदि 10-सेकंड की अवधि में लगातार 5 विफलताएं या 50% त्रुटि दर होती है, तो सर्किट 'ओपन' स्थिति में चला जाता है और डाउनस्ट्रीम सेवा को कॉल करना तुरंत बंद कर देता है।",
            "doc_te": "మైక్రోసర్వీసుల్లో లోపాలు వ్యాపించకుండా నిరోధించడానికి సర్క్యూట్ బ్రేకర్ పద్ధతిని ఉపయోగిస్తారు. 10 సెకన్ల విండోలో వరుసగా 5 వైఫల్యాలు లేదా 50% ఎర్రర్ రేట్ సంభవించినట్లయితే, సర్క్యూట్ బ్రేకర్ 'ఓపెన్' స్థితిలోకి మారుతుంది. ఇది డౌన్‌స్ట్రీమ్ సర్వర్‌కు రిక్వెస్ట్‌లను పంపడం ఆపివేసి తక్షణమే ఫెయిల్-ఫాస్ట్ రెస్పాన్స్‌ను అందిస్తుంది.",
            "doc_teen": "Cascading outages prevent cheyadaniki microservices lo circuit breakers (Resilience4j) deploy chestharu. Rolling 10-second window lo consecutive ga 5 failures kani 50% error rate exceed ayithe circuit breaker 'Open' state ki velthundi, requests ni downstream ki forward cheyakunda ventane fail-fast response isthundi."
        },
        {
            "topic": "Serverless Provisioned Concurrency",
            "task_en": "How does provisioned concurrency eliminate cold start latency in serverless cloud functions?",
            "task_hi": "प्रोविजन्ड कॉनक्रेन्सी सर्वरलेस क्लाउड फ़ंक्शंस में कोल्ड स्टार्ट लेटेंसी को कैसे समाप्त करती है?",
            "task_te": "సర్వర్‌లెస్ క్లౌడ్ ఫంక్షన్లలో కోల్డ్ స్టార్ట్ సమస్యను ప్రొవిజన్డ్ కాన్‌కరెన్సీ ఎలా నివారిస్తుంది?",
            "task_teen": "Serverless Lambda lo provisioned concurrency cold start latency ni ela mitigate chesthundi?",
            "doc_en": "Serverless execution environments incur initial initialization latency ('cold starts') when provisioning new execution containers and loading runtime runtimes. Configuring AWS Lambda Provisioned Concurrency keeps a pre-allocated pool of microVM execution environments initialized and running in a warm state with application code loaded, guaranteeing sub-10 millisecond execution latencies for critical user APIs.",
            "doc_hi": "सर्वरलेस वातावरण में नए कंटेनर शुरू करते समय शुरुआती देरी ('कोल्ड स्टार्ट') होती है। प्रोविजन्ड कॉनक्रेन्सी पहले से ही तैयार और वार्म स्थिति में कंटेनरों का एक पूल रखती है, जिससे महत्वपूर्ण एपीआई के लिए 10 मिलीसेकंड से कम की लेटेंसी सुनिश्चित होती है।",
            "doc_te": "సర్వర్‌లెస్ ఫంక్షన్లలో కొత్త కంటైనర్‌ను ప్రారంభించేటప్పుడు ప్రారంభ ఆలస్యం ('కోల్డ్ స్టార్ట్') ఏర్పడుతుంది. AWS Lambda లో ప్రొవిజన్డ్ కాన్‌కరెన్సీని కాన్ఫిగర్ చేయడం ద్వారా ముందే కేటాయించిన వర్చువల్ మెషీన్లను రన్ చేసి సిద్ధంగా (వార్మ్ స్టేట్) ఉంచుతారు. దీనివల్ల రిక్వెస్ట్ వచ్చినప్పుడు 10 మిల్లీసెకన్ల కంటే తక్కువ సమయంలో వేగంగా రెస్పాన్స్ లభిస్తుంది.",
            "doc_teen": "Serverless functions lo execution container initial loading valla 'cold start' latency vastundi. Provisioned Concurrency configure chesthe pre-warmed execution environments ready ga untayi with application code loaded. Deeni valla critical user APIs ki latency sub-10 milliseconds lo fast ga execute avtundi."
        },
        {
            "topic": "Git Branch Protection Review Rules",
            "task_en": "How many approving peer reviews and checks are required to merge code into main?",
            "task_hi": "कोड को मुख्य शाखा में विलय करने के लिए कितने सहकर्मी समीक्षाओं और जांचों की आवश्यकता होती है?",
            "task_te": "కోడ్‌ను మెయిన్ బ్రాంచ్‌లో మెర్జ్ చేయడానికి ఎన్ని అప్రూవల్స్ మరియు తనిఖీలు తప్పనిసరి?",
            "task_teen": "Git main branch lo code merge cheyali ante enni approving reviews mariyu checks kavali?",
            "doc_en": "Enterprise repository governance enforces branch protection rules on the primary production branch. Direct git pushes to 'main' are disabled. Merging a pull request requires at least 2 independent approving reviews from senior repository maintainers, all CI automated testing checks passing, dismissal of stale reviews upon new commits, and strict rebase or squash commit hygiene.",
            "doc_hi": "उत्पादन शाखा पर सीधी कोड पुश अक्षम है। मुख्य शाखा में पुल अनुरोध को विलय करने के लिए कम से कम 2 वरिष्ठ इंजीनियरों की स्वीकृति, सभी सीआई परीक्षणों का पास होना और नई कमिट पर पुरानी समीक्षाओं का खारिज होना आवश्यक है।",
            "doc_te": "సంస్థ యొక్క గిట్ రెపోజిటరీ నిబంధనల ప్రకారం మెయిన్ ప్రొడక్షన్ బ్రాంచ్‌కు నేరుగా కోడ్ పుష్ చేయడాన్ని నిలిపివేశారు. పుల్ రిక్వెస్ట్‌ను మెర్జ్ చేయాలంటే కనీసం ఇద్దరు సీనియర్ ఇంజనీర్ల ఆమోదం, అన్ని ఆటోమేటెడ్ CI టెస్టులు పాస్ కావడం మరియు కొత్త కమిట్ వచ్చినప్పుడు పాత రివ్యూలను డిస్మిస్ చేయడం తప్పనిసరి.",
            "doc_teen": "Repository governance prakaram 'main' production branch ki direct git push disable chestharu. Pull request merge cheyali ante at least 2 independent approving reviews kavali senior devs nunchi, CI tests anni green ga pass avvali mariyu new commits vachinappudu stale reviews invalidate avtayi."
        }
    ]
}

BUILDER1_DOMAINS = [D1, D2, D3, D4, D5]
