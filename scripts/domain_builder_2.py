"""
Domain Builder 2: Scenarios S051 to S100 (Domains 6 to 10).
Domains:
6. cybersecurity_identity (S051 - S060)
7. ecommerce_retail (S061 - S070)
8. travel_hospitality (S071 - S080)
9. legal_compliance (S081 - S090)
10. customer_support (S091 - S100)
"""

# Domain 6: Cybersecurity & Identity Access Management (S051 - S060)
D6 = {
    "domain": "cybersecurity_identity",
    "scenarios": [
        {
            "topic": "Enterprise Password Complexity Standard",
            "task_en": "What are the minimum character length and composition rules for enterprise passwords?",
            "task_hi": "एंटरप्राइज़ पासवर्ड के लिए न्यूनतम वर्ण लंबाई और संरचना नियम क्या हैं?",
            "task_te": "కార్పొరేట్ పాస్‌వర్డ్‌ల కోసం నిర్దేశించిన కనీస అక్షరాల పొడవు మరియు నిబంధనలు ఏమిటి?",
            "task_teen": "Enterprise password complexity lo minimum character length mariyu rules emiti?",
            "doc_en": "Corporate information security policy mandates that all employee domain credentials contain a minimum length of 14 characters. Passwords must include at least one uppercase letter, one lowercase letter, one numerical digit, and one approved special symbol (e.g., !@#$%^&*). Passwords expire automatically every 90 days, and the identity system prevents reuse of the previous 12 historical passwords.",
            "doc_hi": "कॉर्पोरेट सूचना सुरक्षा नीति के तहत सभी कर्मचारियों के पासवर्ड में न्यूनतम 14 वर्ण होने चाहिए। पासवर्ड में कम से कम एक बड़ा अक्षर, एक छोटा अक्षर, एक संख्या और एक विशेष प्रतीक शामिल होना चाहिए। पासवर्ड हर 90 दिनों में समाप्त हो जाते हैं और पिछले 12 पासवर्ड का पुन: उपयोग नहीं किया जा सकता।",
            "doc_te": "కార్పొరేట్ సమాచార భద్రతా విధానం ప్రకారం ఉద్యోగుల పాస్‌వర్డ్‌లు కనీసం 14 అక్షరాల పొడవును కలిగి ఉండాలి. పాస్‌వర్డ్‌లో కనీసం ఒక పెద్ద అక్షరం (అప్పర్‌కేస్), ఒక చిన్న అక్షరం (లోయర్‌కేస్), ఒక సంఖ్య మరియు ఒక ప్రత్యేక చిహ్నం ఉండాలి. ప్రతి 90 రోజులకు పాస్‌వర్డ్ గడువు ముగుస్తుంది మరియు మునుపటి 12 పాత పాస్‌వర్డ్‌లను మళ్లీ ఉపయోగించలేరు.",
            "doc_teen": "Information security policy prakaram employee domain passwords minimum 14 characters length undali. Mandatory ga at least one uppercase, one lowercase, one digit mariyu one special symbol include cheyali. Passwords prathi 90 days ki expire avtayi mariyu previous 12 historical passwords reuse cheyadam system allow cheyadhu."
        },
        {
            "topic": "Multi-Factor Authentication Enforcement",
            "task_en": "What authentication factors are acceptable for multi-factor enrollment?",
            "task_hi": "मल्टी-फैक्टर नामांकन के लिए कौन से प्रमाणीकरण कारक स्वीकार्य हैं?",
            "task_te": "మల్టీ-ఫ్యాక్టర్ ప్రామాణీకరణ (MFA) నమోదు కోసం ఏ పద్ధతులను అనుమతిస్తారు?",
            "task_teen": "Multi-factor authentication (MFA) enrollment kosam acceptable factors emiti?",
            "doc_en": "All employees accessing internal corporate cloud applications must enroll in phishing-resistant Multi-Factor Authentication (MFA). Permissible second factors include FIDO2 hardware security tokens (e.g., YubiKey) and verified time-based one-time password (TOTP) authenticator applications with biometric device lock. Insecure SMS text message OTP verification is strictly prohibited for production system administration.",
            "doc_hi": "आंतरिक क्लाउड अनुप्रयोगों तक पहुँचने वाले सभी कर्मचारियों को फ़िशिंग-प्रतिरोधी बहु-कारक प्रमाणीकरण (MFA) में नामांकन करना होगा। स्वीकार्य कारकों में FIDO2 हार्डवेयर सुरक्षा टोकन और बायोमेट्रिक लॉक वाले TOTP ऐप शामिल हैं। उत्पादन प्रणालियों के लिए असुरक्षित एसएमएस ओटीपी पूरी तरह से प्रतिबंधित है।",
            "doc_te": "అంతర్గత కార్పొరేట్ క్లౌడ్ అప్లికేషన్లను యాక్సెస్ చేసే ఉద్యోగులందరూ తప్పనిసరిగా ఫిషింగ్-రెసిస్టెంట్ మల్టీ-ఫ్యాక్టర్ అథెంటికేషన్ (MFA) నమోదు చేసుకోవాలి. FIDO2 హార్డ్‌వేర్ సెక్యూరిటీ కీలు (ఉదాహరణకు YubiKey) మరియు బయోమెట్రిక్ లాక్ కలిగిన TOTP ప్రామాణీకరణ యాప్‌లను మాత్రమే అనుమతిస్తారు. ప్రొడక్షన్ సిస్టమ్స్ కోసం అసురక్షిత SMS ఆధారిత OTP పద్ధతిని పూర్తిగా నిషేధించారు.",
            "doc_teen": "Internal corporate cloud applications access cheyali ante phishing-resistant Multi-Factor Authentication (MFA) compulsory. FIDO2 hardware tokens (YubiKey) mariyu biometric locked TOTP authenticator apps matrame allow chestharu. Production administration kosam insecure SMS text OTP use cheyadam strictly prohibited."
        },
        {
            "topic": "Virtual Private Network Inactivity Timeout",
            "task_en": "After how many minutes of idle inactivity does the enterprise corporate VPN disconnect?",
            "task_hi": "कितने मिनट की निष्क्रियता के बाद एंटरप्राइज़ वीपीएन स्वचालित रूप से डिस्कनेक्ट हो जाता है?",
            "task_te": "ఎన్ని నిమిషాల నిష్క్రియాత్మకత తర్వాత కార్పొరేట్ VPN కనెక్షన్ డిస్‌కనెక్ట్ అవుతుంది?",
            "task_teen": "Enterprise corporate VPN idle inactivity timeout enni minutes untundi?",
            "doc_en": "Remote workers connecting to internal data centers via the corporate Virtual Private Network (VPN) tunnel are subject to automated session timeout controls. If network telemetry records zero active traffic for a continuous duration of 30 minutes, the VPN client terminates the encrypted tunnel automatically. Furthermore, all active sessions face a hard re-authentication cap after 12 continuous hours.",
            "doc_hi": "कॉर्पोरेट वीपीएन के माध्यम से आंतरिक डेटा केंद्रों से जुड़ने वाले कर्मचारियों के लिए स्वचालित सत्र समय समाप्ति नियंत्रण लागू हैं। यदि लगातार 30 मिनट तक कोई सक्रिय नेटवर्क ट्रैफ़िक नहीं होता है, तो वीपीएन स्वचालित रूप से सुरंग को बंद कर देता है। इसके अतिरिक्त, सभी सत्र 12 घंटे बाद समाप्त हो जाते हैं।",
            "doc_te": "కార్పొరేట్ VPN ద్వారా అంతర్గత డేటా సెంటర్లకు కనెక్ట్ అయ్యే ఉద్యోగులకు ఆటోమేటెడ్ సెషన్ టైమ్‌అవుట్ నిబంధనలు వర్తిస్తాయి. వరుసగా 30 నిమిషాల పాటు ఎలాంటి నెట్‌వర్క్ ట్రాఫిక్ లేకపోతే VPN క్లయింట్ ఆటోమేటిక్‌గా కనెక్షన్‌ను రద్దు చేస్తుంది. అంతేకాకుండా, నిరంతరంగా 12 గంటల కనెక్షన్ తర్వాత మళ్లీ లాగిన్ కావడం తప్పనిసరి.",
            "doc_teen": "Corporate Virtual Private Network (VPN) use chese remote workers ki automated idle session timeout untundi. Continuous ga 30 minutes active network traffic lekapothe VPN tunnel automatically terminate avtundi. Daanitho paatu prathi 12 hours continuous connection tharuvatha mandatory re-authentication cap untundi."
        },
        {
            "topic": "Security Incident Severity P1 Triage Response SLA",
            "task_en": "What is the mandatory first response time for a Severity 1 (P1) cybersecurity incident?",
            "task_hi": "गंभीरता 1 (P1) साइबर सुरक्षा घटना के लिए अनिवार्य पहली प्रतिक्रिया समय क्या है?",
            "task_te": "తీవ్రత 1 (P1) సైబర్ సెక్యూరిటీ సంఘటనకు మొదటి స్పందన సమయం (SLA) ఎంత?",
            "task_teen": "Severity 1 (P1) cybersecurity incident ki mandatory first response triage SLA entha?",
            "doc_en": "The enterprise Security Operations Center (SOC) classifies incidents based on impact and data sensitivity. A Priority 1 (P1) Critical Incident—defined as active ransomware deployment, root server compromise, or verified customer data exfiltration—mandates on-call incident response engagement within 15 minutes of automated alert firing. The incident commander must assemble the war room and brief executive leadership within 60 minutes.",
            "doc_hi": "एंटरप्राइज़ सुरक्षा संचालन केंद्र (SOC) गंभीरता के आधार पर घटनाओं को वर्गीकृत करता है। प्राथमिकता 1 (P1) गंभीर घटना (जैसे रैंसमवेयर या डेटा चोरी) में अलर्ट मिलने के 15 मिनट के भीतर प्रतिक्रिया देना अनिवार्य है। घटना कमांडर को 60 मिनट के भीतर नेतृत्व को जानकारी देनी होगी।",
            "doc_te": "ఎంటర్‌ప్రైజ్ సెక్యూరిటీ ఆపరేషన్స్ సెంటర్ (SOC) సంఘటనల తీవ్రతను బట్టి వర్గీకరిస్తుంది. ప్రయారిటీ 1 (P1) క్రిటికల్ ఇన్సిడెంట్ (రాన్సమ్‌వేర్ దాడి లేదా డేటా లీక్ వంటివి) సంభవించినప్పుడు హెచ్చరిక వచ్చిన 15 నిమిషాల్లోగా ఇన్సిడెంట్ రెస్పాన్స్ బృందం రంగంలోకి దిగాలి. ఇన్సిడెంట్ కమాండర్ 60 నిమిషాల్లో ఉన్నతాధికారులకు పూర్తి వివరాలు అందించాలి.",
            "doc_teen": "Enterprise SOC incidents ni severity batti categorize chesthundi. Priority 1 (P1) Critical incident (active ransomware, root compromise kani data leak) trigger ayinappudu alert vachina 15 minutes lo incident response team engage avvali. Incident commander 60 minutes lo executive leadership ki briefing submit cheyali."
        },
        {
            "topic": "Privileged Access Just-in-Time Elevation",
            "task_en": "How long do elevated administrative credentials remain active under Just-in-Time PAM?",
            "task_hi": "जस्ट-इन-टाइम PAM के तहत उन्नत प्रशासनिक क्रेडेंशियल कितने समय तक सक्रिय रहते हैं?",
            "task_te": "జస్ట్-ఇన్-టైమ్ PAM విధానంలో అడ్మినిస్ట్రేటర్ అధికారాలు ఎంత సమయం వరకు చెల్లుతాయి?",
            "task_teen": "Just-in-Time Privileged Access Management (PAM) lo elevated credentials validity entha?",
            "doc_en": "To adhere to the principle of least privilege, production infrastructure uses Just-in-Time (JIT) Privileged Access Management. Engineers request temporary root or cluster-admin access tied to an approved change ticket. Upon peer approval, temporary credentials with elevated rights are dynamically generated for a maximum duration of 4 hours, after which all active tokens and bastion SSH keys are automatically revoked.",
            "doc_hi": "उत्पादन प्रणालियों में सुरक्षा के लिए जस्ट-इन-टाइम (JIT) विशेषाधिकार प्रबंधन का उपयोग किया जाता है। इंजीनियर परिवर्तन टिकट से जुड़े अस्थायी रूट एक्सेस का अनुरोध करते हैं। स्वीकृति मिलने पर, उन्नत अधिकार अधिकतम 4 घंटे की अवधि के लिए दिए जाते हैं, जिसके बाद टोकन स्वचालित रूप से रद्द हो जाते हैं।",
            "doc_te": "కనిష్ట అధికారాల సూత్రం ప్రకారం ప్రొడక్షన్ సర్వర్లలో జస్ట్-ఇన్-టైమ్ (JIT) ప్రివిలేజ్డ్ యాక్సెస్ మేనేజ్‌మెంట్ విధానాన్ని అమలు చేస్తారు. ఇంజనీర్లు టికెట్ ఆధారంగా తాత్కాలిక రూట్ యాక్సెస్ కోరవచ్చు. ఆమోదం లభించిన తర్వాత గరిష్టంగా 4 గంటల కాలపరిమితికి మాత్రమే ఈ అధికారాలు లభిస్తాయి, ఆ తర్వాత అన్ని టోకెన్లు ఆటోమేటిక్‌గా రద్దవుతాయి.",
            "doc_teen": "Least privilege policy prakaram production infrastructure lo Just-in-Time (JIT) PAM use chestharu. Approved change ticket tho temporary root access request chesukovachu. Peer approval vachaka temporary elevated credentials maximum 4 hours duration validate avtayi, taruvatha SSH keys mariyu tokens revoke avtayi."
        },
        {
            "topic": "Firewall Default Inbound Ingress Rules",
            "task_en": "What is the default policy for inbound ingress traffic across perimeter firewalls?",
            "task_hi": "परिधि फ़ायरवॉल पर इनबाउंड ट्रैफ़िक के लिए डिफ़ॉल्ट नीति क्या है?",
            "task_te": "నెట్‌వర్క్ పెరిమీటర్ ఫైర్‌వాల్స్‌లో ఇన్‌బౌండ్ ట్రాఫిక్ కోసం ప్రామాణిక డిఫాల్ట్ పాలసీ ఏమిటి?",
            "task_teen": "Perimeter firewalls lo inbound ingress traffic kosam default policy emiti?",
            "doc_en": "Enterprise zero-trust architecture enforces a strict 'Default Deny' stance for all incoming external network traffic across production firewalls and cloud security groups. All inbound ports and protocols are blocked by default unless an explicit, documented security exception ticket is signed off by the cybersecurity team, restricting ingress to specific source IP CIDR blocks and encrypted protocols such as HTTPS (Port 443).",
            "doc_hi": "एंटरप्राइज़ ज़ीरो-ट्रस्ट आर्किटेक्चर सभी आने वाले बाहरी नेटवर्क ट्रैफ़िक के लिए एक सख्त 'डिफ़ॉल्ट अस्वीकार' (Default Deny) नीति लागू करता है। सभी इनबाउंड पोर्ट डिफ़ॉल्ट रूप से अवरुद्ध हैं जब तक कि सुरक्षा टीम द्वारा स्पष्ट अपवाद को मंजूरी नहीं दी जाती है।",
            "doc_te": "ఎంటర్‌ప్రైజ్ జీరో-ట్రస్ట్ ఆర్కిటెక్చర్ ప్రకారం అన్ని నెట్‌వర్క్ ఫైర్‌వాల్స్‌లో ఇన్‌బౌండ్ ట్రాఫిక్‌కు కఠినమైన 'డిఫాల్ట్ డినై' (Default Deny) నియమాన్ని అమలు చేస్తారు. ప్రత్యేకంగా అనుమతించబడిన సెక్యూరిటీ టికెట్ మరియు సెక్యూరిటీ టీమ్ ఆమోదం ఉంటే తప్ప అన్ని ఇన్‌కమింగ్ పోర్టులు మరియు ప్రోటోకాల్స్ సహజంగానే బ్లాక్ చేయబడి ఉంటాయి.",
            "doc_teen": "Zero-trust architecture lo production firewalls mariyu cloud security groups lo incoming external traffic ki strict 'Default Deny' policy untundi. Cybersecurity team formally approve chesina exceptions unte thappa all inbound ports block avtayi, access ni specific source IP blocks mariyu HTTPS (Port 443) ki restrict chestharu."
        },
        {
            "topic": "Suspicious Login Anomaly Lockouts",
            "task_en": "What triggers an automated account security lockout during suspicious login attempts?",
            "task_hi": "संदेहास्पद लॉगिन प्रयासों के दौरान स्वचालित खाता सुरक्षा लॉकआउट क्या ट्रिगर करता है?",
            "task_te": "అనుమానాస్పద లాగిన్ ప్రయత్నాలు జరిగినప్పుడు ఆటోమేటిక్ ఖాతా లాకౌట్‌ను ఏ అంశాలు ట్రిగ్గర్ చేస్తాయి?",
            "task_teen": "Suspicious login attempts jariginappudu automated account lockout trigger chese rules emiti?",
            "doc_en": "The identity risk engine evaluates continuous telemetry for anomalous authentication signals. An automated defensive security lockout is triggered if an account records 5 consecutive failed password attempts within 10 minutes, or exhibits an 'Impossible Travel' velocity anomaly (e.g., successful logins originating from two distant geographic nations within 60 minutes). Accounts remain locked for 30 minutes pending administrator or self-service MFA verification.",
            "doc_hi": "पहचान जोखिम इंजन असामान्य प्रमाणीकरण संकेतों पर नज़र रखता है। यदि कोई खाता 10 मिनट के भीतर लगातार 5 बार विफल पासवर्ड प्रयास दर्ज करता है, या 60 मिनट के भीतर दो अलग-अलग देशों से लॉगिन करता है, तो खाता 30 मिनट के लिए लॉक हो जाता है।",
            "doc_te": "గుర్తింపు భద్రతా వ్యవస్థ లాగిన్ విధానాలను నిరంతరం పర్యవేక్షిస్తుంది. 10 నిమిషాల వ్యవధిలో వరుసగా 5 సార్లు తప్పుడు పాస్‌వర్డ్ నమోదు చేసినా, లేదా 60 నిమిషాల వ్యవధిలో వేర్వేరు దేశాల నుండి లాగిన్ ప్రయత్నాలు (ఇంపాజిబుల్ ట్రావెల్) జరిగినా ఖాతా ఆటోమేటిక్‌గా లాక్ చేయబడుతుంది. అడ్మిన్ లేదా MFA ద్వారా ధృవీకరించే వరకు ఖాతా 30 నిమిషాలు లాక్‌లోనే ఉంటుంది.",
            "doc_teen": "Identity risk engine anomalous authentication ni track chesthundi. 10 minutes lo 5 consecutive failed passwords kani 'Impossible Travel' anomaly (60 mins lo two different distant countries nunchi logins) kanipisthe account automated ga lock avtundi. Admin review kani MFA verification chese varaku account 30 minutes locked ga untundi."
        },
        {
            "topic": "Corporate Data Classification Tiers",
            "task_en": "List the four official corporate data classification levels and their handling requirements.",
            "task_hi": "चार आधिकारिक कॉर्पोरेट डेटा वर्गीकरण स्तरों और उनकी प्रबंधन आवश्यकताओं की सूची बनाएं।",
            "task_te": "నాలుగు అధికారిక కార్పొరేట్ డేటా వర్గీకరణ స్థాయిలను మరియు వాటి నిర్వహణ నిబంధనలను తెలపండి.",
            "task_teen": "Four official corporate data classification tiers mariyu handling requirements emiti?",
            "doc_en": "Corporate data governance categorizes all electronic records into four distinct classification tiers: Public (marketing and press releases, freely shareable); Internal (operational documentation, restricted to authenticated staff); Confidential (source code, customer PII, requiring AES-256 encryption at rest); and Restricted (cryptographic master keys, trade secrets, requiring multi-party authorization and hardware isolation).",
            "doc_hi": "कॉर्पोरेट डेटा को चार स्तरों में वर्गीकृत किया गया है: सार्वजनिक (विपणन सामग्री); आंतरिक (कर्मचारियों तक सीमित); गोपनीय (ग्राहक डेटा, एईएस-256 एन्क्रिप्शन आवश्यक); और प्रतिबंधित (मास्टर कुंजियां और व्यापार रहस्य, हार्डवेयर अलगाव आवश्यक)।",
            "doc_te": "కార్పొరేట్ డేటా గవర్నెన్స్ మొత్తం సమాచారాన్ని నాలుగు విభాగాలుగా వర్గీకరిస్తుంది: పబ్లిక్ (మార్కెటింగ్ మరియు ప్రెస్ నోట్స్, అందరికీ అందుబాటులో ఉంటుంది); ఇంటర్నల్ (సంస్థ అంతర్గత పత్రాలు, ఉద్యోగులకే పరిమితం); కాన్ఫిడెన్షియల్ (కస్టమర్ వ్యక్తిగత సమాచారం, తప్పనిసరిగా AES-256 ఎన్‌క్రిప్షన్ ఉండాలి); మరియు రెస్ట్రిక్టెడ్ (మాస్టర్ సెక్యూరిటీ కీలు మరియు వాణిజ్య రహస్యాలు, అత్యంత కఠినమైన భద్రత అవసరం).",
            "doc_teen": "Corporate data governance lo four distinct tiers untayi: Public (marketing materials, freely shareable); Internal (operational docs for staff only); Confidential (source code, customer PII, requires AES-256 encryption); mariyu Restricted (cryptographic master keys, trade secrets, requires hardware isolation)."
        },
        {
            "topic": "Critical Vulnerability Patching SLA",
            "task_en": "What is the mandatory remediation SLA for critical Common Vulnerabilities and Exposures (CVEs)?",
            "task_hi": "गंभीर सामान्य कमजोरियों और जोखिमों (सीवीई) के लिए अनिवार्य उपचार समय सीमा क्या है?",
            "task_te": "తీవ్రమైన సాఫ్ట్‌వేర్ సెక్యూరిటీ లోపాలను (CVEs) పరిష్కరించడానికి నిర్దేశించిన గడువు ఎంత?",
            "task_teen": "Critical vulnerabilities (CVE score >= 9.0) patch cheyadaniki remediation SLA entha?",
            "doc_en": "The enterprise vulnerability management standard mandates rigorous remediation timelines based on CVSS v3 base severity scores. Critical zero-day vulnerabilities (CVSS 9.0 to 10.0) with public exploit availability must be remediated or mitigated across all production assets within 24 hours of vendor patch release. High severity flaws (CVSS 7.0 to 8.9) require deployment within 7 calendar days.",
            "doc_hi": "गंभीर जीरो-डे कमजोरियों (सीवीएसएस 9.0 से 10.0) को पैच जारी होने के 24 घंटों के भीतर सभी उत्पादन प्रणालियों पर ठीक या कम किया जाना चाहिए। उच्च गंभीरता वाली खामियों (सीवीएसएस 7.0 से 8.9) को 7 दिनों के भीतर ठीक करना आवश्यक है।",
            "doc_te": "సంస్థ యొక్క లోపాల నిర్వహణ విధానం ప్రకారం CVSS v3 స్కోరు ఆధారంగా పరిష్కార గడువులను నిర్ణయిస్తారు. పబ్లిక్ ఎక్స్‌ప్లాయిట్ కలిగిన అత్యంత తీవ్రమైన జీరో-డే లోపాలను (CVSS 9.0 నుండి 10.0) ప్యాచ్ విడుదలైన 24 గంటల్లోగా ప్రొడక్షన్ సర్వర్లలో ఇన్‌స్టాల్ చేయాలి. హై-సివియారిటీ లోపాలను (CVSS 7.0 నుండి 8.9) 7 రోజుల్లోగా పరిష్కరించాలి.",
            "doc_teen": "Vulnerability management standard prakaram CVSS v3 score batti timelines untayi. Critical zero-day vulnerabilities (CVSS 9.0 to 10.0) unte vendor patch release ayina 24 hours lo production lo deploy cheyali. High severity flaws (CVSS 7.0 to 8.9) unte 7 calendar days lo remediation complete cheyadam mandatory."
        },
        {
            "topic": "Endpoint Antivirus Health Compliance",
            "task_en": "How often must managed endpoints synchronize antivirus signature definitions to maintain network access?",
            "task_hi": "नेटवर्क एक्सेस बनाए रखने के लिए प्रबंधित एंडपॉइंट्स को कितनी बार एंटीवायरस परिभाषाओं को सिंक्रनाइజ్ करना होगा?",
            "task_te": "కార్పొరేట్ నెట్‌వర్క్ యాక్సెస్ పొందడానికి కంప్యూటర్లలో యాంటీవైరస్ వివరాలు ఎంత తరచుగా అప్‌డేట్ కావాలి?",
            "task_teen": "Network access maintain cheyali ante endpoint antivirus definitions entha frequency tho sync avvali?",
            "doc_en": "Enterprise endpoint health compliance ensures that all employee laptops maintain active Endpoint Detection and Response (EDR) sensors. Managed devices must synchronize threat signature definitions and sensor telemetry with the central security cloud at least once every 24 hours. Devices failing to update definitions for more than 72 hours are automatically quarantined from the corporate Wi-Fi and production networks.",
            "doc_hi": "सभी कर्मचारी लैपटॉप पर सक्रिय एंटीवायरस और ईडीआर सेंसर होना अनिवार्य है। उपकरणों को हर 24 घंटे में कम से कम एक बार सुरक्षा क्लाउड के साथ खतरे की परिभाषाओं को सिंक्रनाइज़ करना होगा। 72 घंटे से अधिक पुराने उपकरणों को नेटवर्क से अलग कर दिया जाता है।",
            "doc_te": "కార్పొరేట్ భద్రతా నిబంధనల ప్రకారం ఉద్యోగుల ల్యాప్‌టాప్‌లలో క్రియాశీల ఎండ్‌పాయింట్ డిటెక్షన్ అండ్ రెస్పాన్స్ (EDR) సెన్సార్లు ఉండాలి. అన్ని పరికరాలు ప్రతి 24 గంటలకు ఒకసారైనా సెంట్రల్ సెక్యూరిటీ క్లౌడ్‌తో థ్రెట్ సిగ్నేచర్లను సింక్రొనైజ్ చేయాలి. 72 గంటలకు మించి అప్‌డేట్ కాని పరికరాలను నెట్‌వర్క్ నుండి ఆటోమేటిక్‌గా క్వారంటైన్ చేస్తారు.",
            "doc_teen": "Endpoint compliance policy prakaram employee laptops lo active EDR sensors undali. Managed devices prathi 24 hours ki at least once security cloud tho threat definitions sync cheyali. Definitions 72 hours kante ekkuva out of date unte corporate Wi-Fi mariyu production networks nunchi system automatic ga quarantine avtundi."
        }
    ]
}

# Domain 7: E-Commerce & Retail Operations (S061 - S070)
D7 = {
    "domain": "ecommerce_retail",
    "scenarios": [
        {
            "topic": "Standard Order Return Window",
            "task_en": "Within how many days of delivery may retail products be returned for a refund?",
            "task_hi": "रिफंड के लिए डिलीवरी के कितने दिनों के भीतर खुदरा उत्पादों को वापस किया जा सकता है?",
            "task_te": "డెలివరీ జరిగిన ఎన్ని రోజుల్లోగా వస్తువులను వాపసు (రిటర్న్) చేసి డబ్బులు తిరిగి పొందవచ్చు?",
            "task_teen": "Retail orders return chesi refund claim cheyadaniki return window enni days?",
            "doc_en": "Customers may initiate a product return for full monetary reimbursement within 30 calendar days of confirmed package delivery. Returned merchandise must be completely unused, unaltered, and retained in its original manufacturer packaging with all user manuals, tags, and accessories intact. Perishable foodstuffs, personalized custom engravings, and hygiene-sensitive innerwear are strictly non-returnable.",
            "doc_hi": "ग्राहक डिलीवरी के 30 दिनों के भीतर पूर्ण धनवापसी के लिए उत्पाद वापसी शुरू कर सकते हैं। सामान पूरी तरह से अप्रयुक्त, मूल पैकेजिंग में और सभी टैग के साथ होना चाहिए। खराब होने वाले खाद्य पदार्थ, अनुकूलित सामान और स्वच्छता से जुड़े कपड़ों की वापसी संभव नहीं है।",
            "doc_te": "కస్టమర్లు పార్శిల్ డెలివరీ అయిన 30 క్యాలెండర్ రోజులలోపు వస్తువును వాపసు చేసి పూర్తి డబ్బులను తిరిగి పొందవచ్చు. వాపసు చేసే వస్తువు వాడకుండా, అసలైన ప్యాకింగ్, ట్యాగ్‌లు మరియు యాక్సెసరీలతో ఉండాలి. త్వరగా పాడైపోయే ఆహార పదార్థాలు, కస్టమైజ్ చేసిన వస్తువులు మరియు లోదుస్తులను వాపసు తీసుకోవడం జరగదు.",
            "doc_teen": "Customers delivery confirm ayina 30 calendar days lo product return initiate chesi full refund pondavachu. Item unused ga, original packaging, tags mariyu accessories tho intact ga undali. Perishable food items, customized products mariyu hygiene goods return accept cheyaru."
        },
        {
            "topic": "Customer Refund Processing Timeline",
            "task_en": "How many business days does it take for an approved refund to reflect in the original payment method?",
            "task_hi": "स्वीकृत रिफंड को मूल भुगतान विधि में दिखने में कितने कार्य दिवस लगते हैं?",
            "task_te": "ఆమోదించబడిన రీఫండ్ మొత్తం ఖాతాలో జమ కావడానికి ఎన్ని పని దినాలు పడుతుంది?",
            "task_teen": "Approved refund amount original payment source lo credit avvadaniki enni business days paduthundi?",
            "doc_en": "Upon receipt and physical inspection of returned inventory at the regional fulfillment center, approved customer refunds are processed within 48 hours. The monetary reimbursement is remitted directly to the original tender method. Depending on the issuing financial institution, funds typically reflect in credit card or checking statements within 5 to 7 business days.",
            "doc_hi": "रिटर्न प्राप्त होने और निरीक्षण के बाद, स्वीकृत रिफंड 48 घंटों के भीतर संसाधित किए जाते हैं। बैंक के आधार पर, यह राशि 5 से 7 कार्य दिवसों के भीतर क्रेडिट कार्ड या बैंक खाते में दिखाई देती है।",
            "doc_te": "వాపసు వచ్చిన వస్తువు గోడౌన్‌కు చేరి తనిఖీ పూర్తయిన 48 గంటల్లోగా ఆమోదించబడిన రీఫండ్ ప్రాసెస్ చేయబడుతుంది. డబ్బులు నేరుగా కొనుగోలు చేసిన అసలు చెల్లింపు విధానానికే బదిలీ చేయబడతాయి. సంబంధిత బ్యాంక్ లేదా కార్డు నియమాలను బట్టి సాధారణంగా 5 నుండి 7 పని దినాల్లో ఖాతాలో జమ అవుతాయి.",
            "doc_teen": "Fulfillment center lo returned inventory inspection complete ayina 48 hours lo refund process avtundi. Original payment method ke money remit chestharu. Bank card processing networks batti 5 to 7 business days lo amount statement lo reflect avtundi."
        },
        {
            "topic": "Package Tracking Delivery Milestones",
            "task_en": "What are the four primary tracking milestones updated in customer shipment notifications?",
            "task_hi": "ग्राहक शिपमेंट सूचनाओं में अद्यतन किए गए चार प्राथमिक ट्रैकिंग मील के पत्थर क्या हैं?",
            "task_te": "షిప్‌మెంట్ ట్రాకింగ్‌లో కస్టమర్‌కు చూపించే నాలుగు ప్రధాన దశలు ఏమిటి?",
            "task_teen": "Package tracking system lo four primary shipment milestones emiti?",
            "doc_en": "The automated logistics engine generates continuous milestone updates via SMS and email across four standardized phases: Order Confirmed (payment authorized and order received); Dispatched from Fulfillment Center (inventory picked, packed, and transferred to freight carrier); In Transit to Regional Sort Facility; and Out for Delivery (assigned to local route courier with real-time GPS tracking).",
            "doc_hi": "लॉजिस्टिक्स सिस्टम चार चरणों में अपडेट भेजता है: ऑर्डर कन्फर्म (भुगतान स्वीकृत); पूर्ति केंद्र से भेजा गया (वाहक को सौंपा गया); क्षेत्रीय केंद्र के रास्ते में; और डिलीवरी के लिए निकला (स्थानीय कूरियर द्वारा वास्तविक समय जीपीएस ट्रैकिंग के साथ)।",
            "doc_te": "లాజిస్టిక్స్ వ్యవస్థ నాలుగు ప్రధాన దశల్లో SMS మరియు ఇమెయిల్ ద్వారా సమాచారాన్ని అందిస్తుంది: ఆర్డర్ ఖరారైంది (చెల్లింపు ఆమోదించబడింది); గోడౌన్ నుండి బయలుదేరింది (క్యారియర్‌కు అప్పగించబడింది); రవాణాలో ఉంది (రీజనల్ హబ్‌కు చేరుతోంది); మరియు డెలివరీకి బయలుదేరింది (స్థానిక కొరియర్ ద్వారా ప్రత్యక్ష GPS ట్రాకింగ్).",
            "doc_teen": "Logistics tracking engine four standardized milestones tho updates pampisthundi: Order Confirmed; Dispatched from Fulfillment Center; In Transit to Regional Sort Facility; mariyu Out for Delivery (local courier assigned with live GPS tracking)."
        },
        {
            "topic": "Digital Gift Card Terms and Validity",
            "task_en": "What is the expiration validity and cash redeemability policy for digital gift cards?",
            "task_hi": "डिजिटल उपहार कार्डों के लिए समाप्ति वैधता और नकद मोचन नीति क्या है?",
            "task_te": "డిజిటల్ గిఫ్ట్ కార్డుల కాలపరిమితి మరియు నగదుగా మార్చుకునే నిబంధన ఏమిటి?",
            "task_teen": "Digital gift cards validity period mariyu cash redemption rules enti?",
            "doc_en": "Purchased digital gift cards remain fully valid for redemption across all online catalog merchandise for exactly 12 months from the date of electronic issuance. Gift cards are strictly non-reloadable, non-transferable across accounts once claimed, and cannot be redeemed for physical currency cash equivalents except where mandated by local consumer protection statutes.",
            "doc_hi": "खरीदे गए डिजिटल उपहार कार्ड जारी होने की तारीख से 12 महीने के लिए मान्य हैं। इन्हें दोबारा लोड नहीं किया जा सकता, नकद के लिए भुनाया नहीं जा सकता और दूसरे खाते में स्थानांतरित नहीं किया जा सकता।",
            "doc_te": "కొనుగోలు చేసిన డిజిటల్ గిఫ్ట్ కార్డులు జారీ చేసిన తేదీ నుండి సరిగ్గా 12 నెలల పాటు చెల్లుబాటు అవుతాయి. గిఫ్ట్ కార్డులను తిరిగి రీఛార్జ్ చేయడం కుదరదు, ఇతర ఖాతాలకు బదిలీ చేయలేరు మరియు చట్టప్రకారం తప్పనిసరి అయితే తప్ప నగదుగా మార్చుకోవడానికి వీలులేదు.",
            "doc_teen": "Digital gift cards issue ayina date nunchi exactly 12 months varaku redemption ki valid ga untayi. Gift cards non-reloadable, accounts madhya non-transferable mariyu legal mandate unte thappa physical cash ga redeem cheyadam kudaradhu."
        },
        {
            "topic": "Consumer Electronics Manufacturer Warranty Terms",
            "task_en": "What defects are covered and excluded under the 1-year consumer electronics warranty?",
            "task_hi": "1 वर्ष की उपभोक्ता इलेक्ट्रॉनिक्स वारंटी के तहत कौन से दोष कवर और बहिष्कृत हैं?",
            "task_te": "ఎలక్ట్రానిక్స్ వస్తువులపై ఇచ్చే 1-సంవత్సరం వారంటీలో ఏ లోపాలు కవర్ అవుతాయి మరియు ఏవి మినహాయించబడతాయి?",
            "task_teen": "Consumer electronics 1-year warranty lo em cover avtundi mariyu em exclude chestharu?",
            "doc_en": "Hardware electronic products include a standard 1-year limited manufacturer warranty from original retail invoice date. The warranty protects against inherent component failures, motherboard manufacturing defects, and internal power supply degradation under normal operational usage. Coverage strictly excludes accidental drops, liquid immersion, unauthorized third-party repairs, and cosmetic casing scratches.",
            "doc_hi": "इलेक्ट्रॉनिक उत्पादों में 1 साल की वारंटी शामिल है जो विनिर्माण दोषों और सामान्य उपयोग में हार्डवेयर विफलता को कवर करती है। इसमें आकस्मिक गिरावट, पानी का नुकसान, अनधिकृत मरम्मत और खरोंच शामिल नहीं हैं।",
            "doc_te": "ఎలక్ట్రానిక్ వస్తువులకు కొనుగోలు చేసిన తేదీ నుండి 1 సంవత్సరం పరిమిత వారంటీ లభిస్తుంది. సాధారణ వినియోగంలో జరిగే మదర్‌బోర్డ్ లోపాలు, తయారీ లోపాలు మరియు పవర్ సప్లై సమస్యలు దీని కింద ఉచితంగా రిపేర్ చేయబడతాయి. ప్రమాదవశాత్తు కింద పడటం, నీళ్లలో తడవడం, అనుమతి లేని సర్వీసింగ్ మరియు గీతలు వారంటీ పరిధిలోకి రావు.",
            "doc_teen": "Hardware electronics ki invoice date nunchi 1-year manufacturer warranty untundi. Component failures mariyu manufacturing defects normal usage lo cover avtayi. Accidental physical drops, liquid immersion damage, third-party repairs mariyu scratches warranty nunchi strictly exclude avtayi."
        },
        {
            "topic": "Damaged Goods Delivery Protocol",
            "task_en": "Within how many hours must a customer report physically damaged goods received upon delivery?",
            "task_hi": "डिलीवरी पर प्राप्त क्षतिग्रस्त सामान की सूचना ग्राहक को कितने घंटों के भीतर देनी होगी?",
            "task_te": "డెలివరీ సమయంలో పాడైపోయిన లేదా పగిలిపోయిన వస్తువుల గురించి ఎన్ని గంటల్లోగా ఫిర్యాదు చేయాలి?",
            "task_teen": "Delivery lo damaged goods receive ayithe enni hours lo report cheyali?",
            "doc_en": "In the event a customer receives a parcel exhibiting visible transit crushing or damaged internal contents, a formal damage claim must be lodged through the customer service portal within 48 hours of carrier delivery confirmation. The claimant must submit clear photographs of the outer carton, shipping shipping label, and damaged item. Verified damage claims result in immediate complimentary priority replacement.",
            "doc_hi": "यदि ग्राहक को क्षतिग्रस्त पार्सल प्राप्त होता है, तो डिलीवरी के 48 घंटों के भीतर ग्राहक सेवा पोर्टल पर दावा दर्ज करना होगा। बाहरी पैकेजिंग और क्षतिग्रस्त सामान की तस्वीरें जमा करनी होंगी। सत्यापन के बाद तुरंत नया सामान भेजा जाता है।",
            "doc_te": "కస్టమర్ అందుకున్న పార్శిల్ రవాణాలో దెబ్బతిన్నట్లయితే లేదా పగిలిపోయినట్లయితే, డెలివరీ జరిగిన 48 గంటల్లోగా కస్టమర్ సర్వీస్ పోర్టల్‌లో ఫిర్యాదు చేయాలి. బయటి బాక్స్, షిప్పింగ్ లేబుల్ మరియు దెబ్బతిన్న వస్తువు యొక్క స్పష్టమైన ఫోటోలను అప్‌లోడ్ చేయాలి. వివరాలు సరిచూసిన తర్వాత ఉచితంగా కొత్త వస్తువును పంపిస్తారు.",
            "doc_teen": "Delivery appudu transit damage kanipisthe 48 hours lopala customer support portal lo claim lodge cheyali. Outer box, shipping label mariyu damaged item photos submit cheyadam mandatory. Verification taruvatha immediate complimentary replacement dispatch chestharu."
        },
        {
            "topic": "Shopping Cart Session Reservation Limit",
            "task_en": "How long are high-demand items reserved in an active shopping cart before being released?",
            "task_hi": "उच्च-मांग वाली वस्तुएं जारी होने से पहले कितने समय तक शॉपिंग कार्ट में आरक्षित रहती हैं?",
            "task_te": "ఎక్కువ డిమాండ్ ఉన్న వస్తువులను షాపింగ్ కార్ట్‌లో ఎంత సమయం వరకు రిజర్వ్‌లో ఉంచుతారు?",
            "task_teen": "High-demand flash sale items shopping cart lo enni minutes reserved ga untayi?",
            "doc_en": "During limited promotional flash sales and high-demand product releases, placing an SKU into an active checkout shopping cart places an automated inventory hold for exactly 60 minutes. If the customer does not complete payment processing within this 60-minute checkout reservation window, the lock expires and the units are returned to the available public inventory pool.",
            "doc_hi": "फ़्लैश बिक्री के दौरान, कार्ट में सामान जोड़ने पर वह 60 मिनट के लिए आरक्षित रहता है। यदि इस अवधि के भीतर भुगतान पूरा नहीं होता है, तो आरक्षण समाप्त हो जाता है और सामान अन्य ग्राहकों के लिए उपलब्ध हो जाता है।",
            "doc_te": "ఫ్లాష్ సేల్స్ మరియు అధిక డిమాండ్ ఉన్న సమయంలో వస్తువును షాపింగ్ కార్ట్‌లో చేర్చినప్పుడు ఆ వస్తువు 60 నిమిషాల పాటు రిజర్వ్ చేయబడుతుంది. కస్టమర్ ఈ 60 నిమిషాల వ్యవధిలో చెల్లింపు పూర్తి చేయకపోతే, రిజర్వేషన్ రద్దవుతుంది మరియు ఆ వస్తువు మళ్లీ ఇతరులు కొనుగోలు చేయడానికి విడుదల చేయబడుతుంది.",
            "doc_teen": "Flash sales mariyu high-demand releases lo cart lo item add chesthe exactly 60 minutes inventory hold reservation untundi. Customer 60 minutes checkout window lo payment complete cheyakapothe hold expire ayyi inventory public pool ki release avtundi."
        },
        {
            "topic": "International Customs and Import Duties DDP",
            "task_en": "How are international customs duties and import taxes collected under Delivered Duty Paid (DDP)?",
            "task_hi": "डिलीवर्ड ड्यूटी पेड (डीडीपी) के तहत अंतर्राष्ट्रीय सीमा शुल्क और आयात कर कैसे एकत्र किए जाते हैं?",
            "task_te": "డెలివర్డ్ డ్యూటీ పెయిడ్ (DDP) కింద అంతర్జాతీయ కస్టమ్స్ డ్యూటీ మరియు పన్నులను ఎలా వసూలు చేస్తారు?",
            "task_teen": "Delivered Duty Paid (DDP) shipping lo international customs taxes ela collect chestharu?",
            "doc_en": "Cross-border global e-commerce shipments utilizing Delivered Duty Paid (DDP) shipping calculate all destination customs import duties and local goods and services taxes upfront at electronic checkout. The customer prepays all statutory border charges directly, ensuring the package clears destination customs inspection without the recipient being contacted for supplemental carrier brokerage fees upon arrival.",
            "doc_hi": "डीडीपी शिपिंग का उपयोग करने वाले सीमा पार ऑर्डर चेकआउट के समय ही सभी सीमा शुल्क और स्थानीय करों की गणना करते हैं। ग्राहक पहले ही भुगतान कर देता है, जिससे डिलीवरी के समय कोई अतिरिक्त शुल्क नहीं देना पड़ता है।",
            "doc_te": "డెలివర్డ్ డ్యూటీ పెయిడ్ (DDP) షిప్పింగ్ విధానంలో అంతర్జాతీయ కస్టమ్స్ డ్యూటీ మరియు దిగుమతి పన్నులను కొనుగోలు సమయంలోనే (ఆన్‌లైన్ చెక్‌అవుట్ వద్ద) లెక్కిస్తారు. కస్టమర్ ఈ ఛార్జీలను ముందే చెల్లిస్తారు, దీనివల్ల పార్శిల్ డెలివరీ అయ్యే సమయంలో కస్టమర్ ఎలాంటి అదనపు కస్టమ్స్ రుసుములు చెల్లించాల్సిన అవసరం ఉండదు.",
            "doc_teen": "Cross-border orders Delivered Duty Paid (DDP) shipping use chesthe checkout appude customs import duties calculate chestharu. Customer border charges munde prepay cheyadam valla package destination customs clear chesukoni additional fees lekunda smoothly deliver avtundi."
        },
        {
            "topic": "Customer Loyalty Rewards Point Expiration",
            "task_en": "When do earned loyalty rewards points expire if unused?",
            "task_hi": "यदि उपयोग नहीं किया जाता है तो अर्जित लॉयल्टी रिवार्ड पॉइंट कब समाप्त होते हैं?",
            "task_te": "వాడుకోని లాయల్టీ రివార్డు పాయింట్లు ఎంత కాలానికి రద్దవుతాయి?",
            "task_teen": "Customer loyalty reward points unused ga unte enni months lo expire avtayi?",
            "doc_en": "Registered loyalty rewards members accrue 1 reward point for every qualifying dollar spent across the retail marketplace. Points are accumulated in the customer's digital wallet and remain valid for redemption for 12 months from the date of the qualifying transaction. Unredeemed points automatically lapse on a rolling monthly basis on the final day of the twelfth calendar month.",
            "doc_hi": "लॉयल्टी रिवार्ड पॉइंट लेनदेन की तारीख से 12 महीने के लिए वैध रहते हैं। इस अवधि के भीतर उपयोग नहीं किए जाने पर, बिना रिडीम किए गए पॉइंट बारहवें महीने के अंतिम दिन स्वतः समाप्त हो जाते हैं।",
            "doc_te": "నమోదిత లాయల్టీ సభ్యులు చేసే ప్రతి కొనుగోలుపై రివార్డు పాయింట్లు లభిస్తాయి. ఈ పాయింట్లు కస్టమర్ వాలెట్‌లో జమ చేయబడతాయి మరియు కొనుగోలు చేసిన తేదీ నుండి 12 నెలల పాటు చెల్లుబాటు అవుతాయి. 12 నెలల ముగింపు నాటికి వాడుకోని పాయింట్లు స్వయంచాలకంగా రద్దవుతాయి.",
            "doc_teen": "Loyalty program lo spending pai reward points accrue avtayi. Ee points transaction date nunchi exactly 12 months varaku wallet lo valid ga untayi. Unredeemed points rolling basis lo 12th calendar month last day na automatically lapse avtayi."
        },
        {
            "topic": "Bulk Order Wholesale Discount Thresholds",
            "task_en": "What quantity qualifies commercial buyers for the 15% wholesale discount tier?",
            "task_hi": "कौन सी मात्रा वाणिज्यिक खरीदारों को 15% थोक छूट स्तर के लिए योग्य बनाती है?",
            "task_te": "వ్యాపార కొనుగోలుదారులు 15% హోల్‌సేల్ తగ్గింపు పొందడానికి కనీసం ఎన్ని వస్తువులను ఆర్డర్ చేయాలి?",
            "task_teen": "Bulk purchase lo 15% wholesale discount tier qualify avvali ante order quantity entha undali?",
            "doc_en": "B2B commercial wholesale procurement guidelines establish tiered quantity discounts for volume buyers. Purchase orders containing between 20 and 49 identical catalog units receive an automated 10% invoice discount. Purchase orders exceeding 50 units qualify for the premier 15% wholesale discount and complimentary freight shipping. Wholesale purchases are final sale and exempt from standard 30-day retail return privileges.",
            "doc_hi": "थोक खरीदारों के लिए 20 से 49 इकाइयों के ऑर्डर पर 10% की छूट मिलती है। 50 इकाइयों से अधिक के ऑर्डर 15% की छूट और मुफ्त माल ढुलाई के पात्र हैं। थोक बिक्री अंतिम होती है और वापसी योग्य नहीं होती है।",
            "doc_te": "హోల్‌సేల్ కొనుగోలుదారుల కోసం పరిమాణం ఆధారంగా తగ్గింపులను నిర్ణయించారు. 20 నుండి 49 వస్తువుల ఆర్డర్‌పై 10% తగ్గింపు లభిస్తుంది. 50 లేదా అంతకంటే ఎక్కువ వస్తువులను ఒకేసారి ఆర్డర్ చేస్తే 15% హోల్‌సేల్ డిస్కౌంట్ మరియు ఉచిత రవాణా సౌకర్యం లభిస్తుంది. హోల్‌సేల్ కొనుగోళ్లకు సాధారణ 30 రోజుల వాపసు నిబంధన వర్తించదు.",
            "doc_teen": "Wholesale volume buyers ki tiered discounts untayi: 20 to 49 units order chesthe 10% invoice discount, 50 units kante ekkuva order chesthe 15% wholesale discount plus free freight shipping istharu. Wholesale orders final sale ga treat chestharu, retail returns allow cheyaru."
        }
    ]
}

# Domain 8: Travel, Airlines & Hospitality (S071 - S080)
D8 = {
    "domain": "travel_hospitality",
    "scenarios": [
        {
            "topic": "Airline Cabin Carry-On Allowance",
            "task_en": "What is the maximum permissible weight and dimension for airline cabin carry-on luggage?",
            "task_hi": "हवाई जहाज के केबिन कैरी-ऑन सामान के लिए अधिकतम अनुमेय वजन और आयाम क्या है?",
            "task_te": "విమాన ప్రయాణంలో క్యాబిన్ లగేజీకి అనుమతించబడిన గరిష్ట బరువు మరియు పరిమాణం ఎంత?",
            "task_teen": "Flight cabin carry-on baggage maximum weight mariyu dimensions entha?",
            "doc_en": "Economy class airline passengers are permitted one primary cabin baggage item weighing up to 7 kilograms with linear dimensions not exceeding 55 cm x 40 cm x 20 cm, including wheels and handles. In addition, travelers may bring one compact personal item (such as a laptop bag or handbag) capable of stowing beneath the forward seat. Bags exceeding 7 kilograms must be checked into the cargo hold with applicable baggage fees.",
            "doc_hi": "इकोनॉमी क्लास के यात्रियों को अधिकतम 7 किलोग्राम वजन और 55 x 40 x 20 सेमी आयाम वाले एक केबिन बैग की अनुमति है। इसके अतिरिक्त, एक छोटा लैपटॉप बैग ले जाने की अनुमति है। 7 किलोग्राम से अधिक के बैग को कार्गो में जमा करना होगा।",
            "doc_te": "ఎకానమీ క్లాస్ విమాన ప్రయాణికులు గరిష్టంగా 7 కిలోల బరువు మరియు 55 x 40 x 20 సెం.మీ పరిమాణం కలిగిన ఒక క్యాబిన్ బ్యాగ్‌ను తీసుకెళ్లవచ్చు. దీనితో పాటు ల్యాప్‌టాప్ బ్యాగ్ లేదా చిన్న హ్యాండ్‌బ్యాగ్‌ను ఉచితంగా అనుమతిస్తారు. 7 కిలోల పరిమితి దాటితే ఎయిర్‌పోర్ట్ కౌంటర్‌లో అదనపు రుసుము చెల్లించి చెక్-ఇన్ లగేజీగా పంపాలి.",
            "doc_teen": "Economy passengers ki 7 kg maximum weight mariyu 55 x 40 x 20 cm dimensions unna single cabin bag allow chestharu. Daanitho paatu under-seat laptop bag carry chesukovachu. 7 kg weight exceed ayithe cargo hold lo check-in chesi baggage fees pay cheyali."
        },
        {
            "topic": "Hotel Check-In and Check-Out Schedules",
            "task_en": "What are the standard hotel check-in and check-out times?",
            "task_hi": "होटल में चेक-इन और चेक-आउट का मानक समय क्या है?",
            "task_te": "హోటళ్లలో ప్రామాణిక చెక్-ఇన్ మరియు చెక్-అవుట్ సమయాలు ఏమిటి?",
            "task_teen": "Hotels lo standard check-in mariyu check-out times enti?",
            "doc_en": "Standard international hospitality regulations set hotel room check-in time starting at 2:00 PM local time. Departure check-out is strictly scheduled for 11:00 AM on the day of departure to enable housekeeping disinfection. Early arrivals prior to 10:00 AM or late check-outs past 2:00 PM incur a half-day room surcharge subject to hotel occupancy availability.",
            "doc_hi": "होटल चेक-इन का समय स्थानीय समयानुसार दोपहर 2:00 बजे शुरू होता है और चेक-आउट सुबह 11:00 बजे होता है। सुबह 10:00 बजे से पहले जल्दी आने या दोपहर 2:00 बजे के बाद देर से जाने पर आधे दिन का अतिरिक्त शुल्क लगता है।",
            "doc_te": "అంతర్జాతీయ హోటల్ నిబంధనల ప్రకారం చెక్-ఇన్ సమయం మధ్యాహ్నం 2:00 గంటలకు ప్రారంభమవుతుంది. గదుల శుభ్రత కొరకు నిష్క్రమణ రోజున ఉదయం 11:00 గంటలకే చెక్-అవుట్ చేయాలి. ఉదయం 10:00 గంటలకు ముందే రావడం లేదా మధ్యాహ్నం 2:00 తర్వాత ఆలస్యంగా వెళ్లడం వంటి వాటికి గదుల లభ్యతను బట్టి సగం రోజు అద్దెను వసూలు చేస్తారు.",
            "doc_teen": "Hotel regulations prakaram standard check-in local time 2:00 PM nunchi start avtundi. Check-out departure day morning 11:00 AM lopala compulsory. Early morning 10:00 AM munde check-in kani 2:00 PM tharuvatha late check-out kani chesthe half-day surcharge paduthundi."
        },
        {
            "topic": "Train Ticket Cancellation Refund Rules",
            "task_en": "What refund is granted for train tickets cancelled more than 48 hours prior to departure?",
            "task_hi": "प्रस्थान से 48 घंटे से अधिक पहले रद्द किए गए ट्रेन टिकटों के लिए क्या रिफंड दिया जाता है?",
            "task_te": "రైలు బయలుదేరడానికి 48 గంటల ముందు టికెట్ రద్దు చేసుకుంటే ఎంత రీఫండ్ లభిస్తుంది?",
            "task_teen": "Train departure ki 48 hours munde ticket cancel chesthe refund policy enti?",
            "doc_en": "Confirmed railway passenger reservations cancelled more than 48 hours prior to the scheduled train departure time are granted a full refund of the base fare, subject only to a nominal administrative clerkage cancellation fee ($3 for second class, $5 for air-conditioned berths). Cancellations between 48 hours and 12 hours prior to departure forfeit 25% of fare value, while tickets cancelled less than 4 hours before departure receive zero refund.",
            "doc_hi": "ट्रेन छूटने से 48 घंटे से अधिक पहले रद्द किए गए टिकटों पर क्लर्केज शुल्क काटकर पूरा किराया वापस किया जाता है। 48 से 12 घंटे के बीच रद्द करने पर 25% कटौती होती है, जबकि 4 घंटे से कम समय में रद्द करने पर कोई रिफंड नहीं मिलता है।",
            "doc_te": "రైలు బయలుదేరే సమయానికి 48 గంటల కంటే ముందుగా టికెట్‌ను రద్దు చేసుకుంటే ప్రామాణిక క్లర్కేజ్ రుసుము (సెకండ్ క్లాస్‌కు $3, AC కి $5) మినహాయించి మిగిలిన మొత్తం రుసుమును వాపసు చేస్తారు. 48 నుండి 12 గంటల మధ్య రద్దు చేసుకుంటే 25% కోత విధిస్తారు. రైలు బయలుదేరడానికి 4 గంటల లోపు రద్దు చేసుకుంటే ఎలాంటి రీఫండ్ లభించదు.",
            "doc_teen": "Train departure ki 48 hours munde confirmed ticket cancel chesthe nominal clerkage fee ($3 to $5) deduct chesi full fare refund chestharu. 48 to 12 hours madhyalo 25% cut avtundi, mariyu 4 hours munde cancel chesthe zero refund istharu."
        },
        {
            "topic": "International Passport Validity Rule for Travel",
            "task_en": "How many months of remaining passport validity are required for international border crossing?",
            "task_hi": "अंतर्राष्ट्रीय सीमा पार करने के लिए पासपोर्ट की कितनी शेष वैधता आवश्यक है?",
            "task_te": "అంతర్జాతీయ ప్రయాణాలకు పాస్‌పోర్ట్ కనీసం ఎన్ని నెలల కాలపరిమితి కలిగి ఉండాలి?",
            "task_teen": "International border travel chesetappudu passport minimum remaining validity enni months undali?",
            "doc_en": "International border and civil aviation immigration mandates require foreign travelers to possess a national passport valid for at least 6 months beyond the scheduled date of departure from the destination country. Airlines are legally obligated to deny boarding to any passenger whose travel document expires within the 6-month threshold, regardless of valid tourist visas or confirmed return itineraries.",
            "doc_hi": "अंतर्राष्ट्रीय विमानन नियमों के तहत यात्रियों के पास गंतव्य देश से लौटने की तारीख के बाद भी कम से कम 6 महीने के लिए वैध पासपोर्ट होना चाहिए। 6 महीने से कम वैधता वाले यात्रियों को एयरलाइंस द्वारा उड़ान में चढ़ने से रोक दिया जाता है।",
            "doc_te": "అంతర్జాతీయ విమానయాన మరియు ఇమ్మిగ్రేషన్ నిబంధనల ప్రకారం ప్రయాణికులు సందర్శించే దేశం నుండి తిరిగి వచ్చే తేదీ నుండి కనీసం 6 నెలల చెల్లుబాటు గల పాస్‌పోర్ట్‌ను కలిగి ఉండాలి. పాస్‌పోర్ట్ కాలపరిమితి 6 నెలల కంటే తక్కువగా ఉంటే వీసా ఉన్నప్పటికీ విమాన సంస్థలు ప్రయాణాన్ని నిరాకరిస్తాయి.",
            "doc_teen": "International immigration rules prakaram travel document scheduled departure date tharuvatha kuda minimum 6 months remaining validity undali. Valid visa unna sare passport validity 6 months kante thakkuva unte airlines boarding deny cheyadam legal mandate."
        },
        {
            "topic": "Tourist Visa on Arrival Eligibility",
            "task_en": "What is the maximum duration of stay for a single-entry tourist visa on arrival?",
            "task_hi": "आगमन पर एकल-प्रवेश पर्यटक वीजा (वीजा ऑन अराइवल) के लिए ठहरने की अधिकतम अवधि क्या है?",
            "task_te": "సింగిల్-ఎంట్రీ టూరిస్ట్ వీసా ఆన్ అరైవల్ ద్వారా గరిష్టంగా ఎన్ని రోజులు ఉండవచ్చు?",
            "task_teen": "Single-entry tourist visa on arrival stay duration maximum enni days untundi?",
            "doc_en": "Qualified international tourists arriving at designated international airports may obtain a 30-day single-entry Tourist Visa on Arrival (VoA). Applicants must present a confirmed return flight booking departing within 30 days, documented hotel reservations, and proof of adequate financial solvency ($1,000 per person). The visa may be extended once for an additional 30 days at municipal immigration offices upon payment of the renewal fee.",
            "doc_hi": "पर्यटक आगमन पर 30 दिनों का वीजा (VoA) प्राप्त कर सकते हैं। इसके लिए वापसी का टिकट, होटल बुकिंग और पर्याप्त धन ($1,000) का प्रमाण दिखाना होगा। इसे आव्रजन कार्यालय में शुल्क देकर 30 दिनों के लिए एक बार बढ़ाया जा सकता है।",
            "doc_te": "అర్హత గల అంతర్జాతీయ పర్యాటకులు విమానాశ్రయంలో 30 రోజుల సింగిల్-ఎంట్రీ టూరిస్ట్ వీసా ఆన్ అరైవల్ పొందవచ్చు. దీని కోసం 30 రోజుల్లోపు తిరిగి వెళ్లే రిటర్న్ టికెట్, హోటల్ బుకింగ్ మరియు కనీస నిధుల నిరూపణ ($1,000) చూపించాలి. నిర్ణీత రుసుము చెల్లించి స్థానిక ఇమ్మిగ్రేషన్ ఆఫీసులో మరో 30 రోజులు దీనిని పొడిగించుకోవచ్చు.",
            "doc_teen": "International tourists airport lo 30-day single-entry Tourist Visa on Arrival (VoA) pondavachu. 30 days lopala confirm return flight ticket, hotel reservation mariyu minimum funds ($1,000) proof chupinchali. Local immigration lo fee pay chesi another 30 days extend chesukovachu."
        },
        {
            "topic": "Hotel Room Maximum Occupancy Regulations",
            "task_en": "What is the maximum allowed occupancy for a standard double hotel room?",
            "task_hi": "एक मानक डबल होटल के कमरे के लिए अधिकतम अनुमत अधिभोग क्या है?",
            "task_te": "స్టాండర్డ్ డబుల్ హోటల్ రూమ్‌లో గరిష్టంగా ఎంతమంది నివసించడానికి అనుమతిస్తారు?",
            "task_teen": "Standard double hotel room lo maximum allowed occupancy entha?",
            "doc_en": "Municipal hospitality fire and safety codes restrict the maximum permitted guest occupancy of a standard double room to 2 adults and 1 child under the age of 12 years sharing existing bedding. A third adult guest requires the reservation of an extra rollaway bed subject to a supplementary nightly fee of $40, which includes breakfast. Exceeding room occupancy limits violates local fire evacuation codes.",
            "doc_hi": "सुरक्षा नियमों के अनुसार एक मानक डबल रूम में अधिकतम 2 वयस्क और 12 वर्ष से कम उम्र के 1 बच्चे को रहने की अनुमति है। तीसरे वयस्क के लिए $40 के अतिरिक्त शुल्क पर एक अतिरिक्त बिस्तर की आवश्यकता होती है।",
            "doc_te": "అగ్నిమాపక భద్రతా నిబంధనల ప్రకారం ఒక సాధారణ డబుల్ హోటల్ గదిలో గరిష్టంగా ఇద్దరు పెద్దలు మరియు 12 ఏళ్ల లోపు ఒక చిన్నారి మాత్రమే ఉండవచ్చు. మూడవ వ్యక్తి ఉండాలంటే రోజుకు $40 అదనపు రుసుము చెల్లించి ఎక్స్‌ట్రా బెడ్ తీసుకోవాలి. నిబంధనలను మించి ఎక్కువ మంది ఉండటం అగ్నిమాపక చట్టాల ఉల్లంఘన కిందకు వస్తుంది.",
            "doc_teen": "Fire and safety regulations prakaram standard double room lo max occupancy 2 adults mariyu 1 child (below 12 years) matrame. Third adult undali ante $40 per night extra rollaway bed charge pay cheyali. Occupancy limit exceed chesthe fire safety violations trigger avtayi."
        },
        {
            "topic": "Travel Insurance Trip Cancellation Coverage",
            "task_en": "What unforeseen events qualify for full trip cancellation reimbursement under travel insurance?",
            "task_hi": "यात्रा बीमा के तहत कौन सी अप्रत्याशित घटनाएं पूर्ण यात्रा रद्दीकरण प्रतिपूर्ति के लिए योग्य हैं?",
            "task_te": "ట్రావెల్ ఇన్సూరెన్స్ కింద టికెట్ రద్దు ఖర్చులను తిరిగి పొందడానికి ఏ పరిస్థితులను పరిగణిస్తారు?",
            "task_teen": "Travel insurance lo full trip cancellation reimbursement claim cheyadaniki covered events emiti?",
            "doc_en": "Comprehensive travel insurance policies reimburse non-refundable, prepaid airline tickets and hotel deposits up to the contracted policy limit ($5,000) if a trip is cancelled prior to departure due to a covered peril. Recognized qualifying events include sudden severe illness or injury certified by an attending physician, death of an immediate family member, or severe weather causing complete carrier shutdown for over 24 hours.",
            "doc_hi": "यात्रा बीमा पूर्व-भुगतान की गई टिकटों और होटल बुकिंग की प्रतिपूर्ति करता है यदि यात्रा अचानक बीमारी, परिवार में मृत्यु या 24 घंटे से अधिक समय तक खराब मौसम के कारण रद्द हो जाती है।",
            "doc_te": "ట్రావెల్ ఇన్సూరెన్స్ పాలసీలు ప్రయాణానికి ముందే ఊహించని కారణాల వల్ల రద్దయిన నాన్-రీఫండబుల్ విమాన టికెట్లు మరియు హోటల్ ఖర్చులను $5,000 పరిమితి వరకు రీయింబర్స్ చేస్తాయి. డాక్టర్ ధృవీకరించిన ఆకస్మిక తీవ్ర అనారోగ్యం, కుటుంబ సభ్యుల మరణం లేదా తుఫానుల వల్ల 24 గంటలకు మించి విమాన సర్వీసులు నిలిచిపోవడం వంటివి దీని కింద కవర్ అవుతాయి.",
            "doc_teen": "Comprehensive travel insurance pre-paid non-refundable tickets mariyu hotel deposits ni policy limit ($5,000) varaku reimburse chesthundi. Certified severe medical illness, immediate family member demise, kani extreme weather valla 24 hours flights cancel ayithe covered events ga consider chestharu."
        },
        {
            "topic": "Rental Car Security Deposit Release",
            "task_en": "How long does it take for a vehicle rental security deposit pre-authorization to be released?",
            "task_hi": "वाहन किराए पर लेने की सुरक्षा जमा राशि जारी होने में कितना समय लगता है?",
            "task_te": "కారు అద్దెకు తీసుకున్నప్పుడు బ్లాక్ చేసిన సెక్యూరిటీ డిపాజిట్ ఎన్ని గంటల్లో విడుదల అవుతుంది?",
            "task_teen": "Car rental security deposit pre-authorization hold release avvadaniki enni hours paduthundi?",
            "doc_en": "When hiring a vehicle, rental car agencies place a temporary pre-authorization credit card hold of $300 to secure against fuel shortfalls, toll charges, or minor vehicle damage. Upon returning the automobile with an undamaged body and a full fuel tank, the agency releases the pre-authorization within 72 hours. Releasing funds to available credit depends on the customer's issuing banking network.",
            "doc_hi": "कार किराए पर लेते समय $300 की सुरक्षा जमा राशि कार्ड पर रोक ली जाती है। बिना किसी नुकसान और भरे हुए ईंधन के साथ वाहन वापस करने पर 72 घंटों के भीतर यह राशि जारी कर दी जाती है।",
            "doc_te": "కారును అద్దెకు తీసుకునేటప్పుడు ఇంధనం, టోల్ ఫీజులు లేదా చిన్నపాటి నష్టాల నిమిత్తం క్రెడిట్ కార్డుపై $300 సెక్యూరిటీ డిపాజిట్‌ను హోల్డ్ చేస్తారు. ఎలాంటి నష్టం లేకుండా పూర్తి ఇంధనంతో కారును తిరిగి అప్పగించిన 72 గంటల్లోపు ఏజెన్సీ ఆ హోల్డ్‌ను విడుదల చేస్తుంది. కస్టమర్ ఖాతాలో జమ కావడం బ్యాంకును బట్టి ఉంటుంది.",
            "doc_teen": "Car rental hire chesetappudu credit card pai $300 security deposit pre-authorization hold pedతారు. Vehicle undamaged ga full tank fuel tho return chesina 72 hours lo agency hold release chesthundi. Available credit restore avvadam issuing bank timeline pai depend avtundi."
        },
        {
            "topic": "Guided Group Excursion Cancellation Terms",
            "task_en": "What is the cancellation notice period for a 100% refund on guided group excursions?",
            "task_hi": "समूह भ्रमण पर 100% रिफंड के लिए रद्दीकरण सूचना अवधि क्या है?",
            "task_te": "గైడెడ్ గ్రూప్ టూర్లలో 100% పూర్తి రీఫండ్ పొందడానికి ఎన్ని రోజుల ముందుగా రద్దు చేసుకోవాలి?",
            "task_teen": "Guided group tour excursion 100% refund tho cancel cheyali ante notice period entha?",
            "doc_en": "Pre-booked guided group sightseeing tours and adventure excursions provide full 100% refunds if cancellation requests are transmitted in writing at least 7 calendar days prior to the excursion departure date. Cancellations received between 6 days and 48 hours prior to start time receive a 50% refund, while cancellations within 48 hours or participant no-shows forfeit the entire booking payment.",
            "doc_hi": "टूर शुरू होने से कम से कम 7 दिन पहले लिखित में रद्द करने पर 100% रिफंड दिया जाता है। 6 दिन से 48 घंटे के बीच 50% रिफंड मिलता है और 48 घंटे से कम समय में कोई रिफंड नहीं दिया जाता है।",
            "doc_te": "ముందుగా బుక్ చేసుకున్న గ్రూప్ టూర్లను ప్రారంభ తేదీకి కనీసం 7 రోజుల ముందుగా రద్దు చేసుకుంటే 100% పూర్తి రుసుము తిరిగి చెల్లించబడుతుంది. 6 రోజుల నుండి 48 గంటల మధ్య రద్దు చేస్తే 50% మాత్రమే వాపసు ఇస్తారు. 48 గంటల లోపు రద్దు చేసినా లేదా టూర్‌కు హాజరు కాకపోయినా ఎలాంటి డబ్బులు తిరిగి ఇవ్వరు.",
            "doc_teen": "Guided group excursions tour date ki 7 calendar days munde cancel chesthe 100% full refund istharu. 6 days nunchi 48 hours madhyalo cancel chesthe 50% refund untundi, 48 hours lopala kani no-show ayina total booking amount forfeit avtundi."
        },
        {
            "topic": "Aviation Flight Delay Meal and Rebooking Compensation",
            "task_en": "What compensation and accommodations are passengers entitled to if a flight is delayed over 4 hours?",
            "task_hi": "यदि किसी उड़ान में 4 घंटे से अधिक की देरी होती है तो यात्री किस मुआवजे और आवास के हकदार हैं?",
            "task_te": "విమానం 4 గంటలకు మించి ఆలస్యమైతే ప్రయాణికులకు లభించే ఉచిత ఆహారం మరియు ప్రత్యామ్నాయ సదుపాయాలు ఏమిటి?",
            "task_teen": "Flight 4 hours kante ekkuva delay ayithe passengers ki meal mariyu compensation rules enti?",
            "doc_en": "Under civil aviation passenger protection mandates, if a scheduled domestic or international flight departure is delayed by more than 4 hours due to airline technical or operational faults, the operating carrier must provide complimentary food and beverage refreshment vouchers. If the delay extends overnight beyond midnight, the airline must arrange complimentary hotel lodging with round-trip ground airport transfers.",
            "doc_hi": "यदि एयरलाइन की गलती के कारण उड़ान में 4 घंटे से अधिक की देरी होती है, तो एयरलाइन को मुफ्त भोजन और जलपान वाउचर प्रदान करना होगा। यदि देरी रात भर जारी रहती है, तो होटल में ठहरने और परिवहन की व्यवस्था करनी होगी।",
            "doc_te": "పౌర విమానయాన నిబంధనల ప్రకారం విమాన సంస్థ సాంకేతిక లోపాల వల్ల విమానం 4 గంటలకు మించి ఆలస్యమైతే ప్రయాణికులకు ఉచిత భోజనం మరియు పానీయాల కూపన్లు అందించాలి. ఒకవేళ ఆలస్యం రాత్రంతా కొనసాగితే ఎయిర్‌పోర్ట్ దగ్గర్లోని హోటల్‌లో ఉచిత బస మరియు ప్రయాణ రవాణా సౌకర్యాలను విమాన సంస్థే స్వయంగా కల్పించాలి.",
            "doc_teen": "Civil aviation passenger mandates prakaram airline fault valla flight 4 hours kante ekkuva delay ayithe free food and beverage refreshment vouchers ivvali. Delay overnight midnight daatithe complimentary hotel accommodation mariyu airport transfers airline arrange cheyali."
        }
    ]
}

# Domain 9: Legal, Privacy & Compliance (S081 - S090)
D9 = {
    "domain": "legal_compliance",
    "scenarios": [
        {
            "topic": "GDPR Right to Erasure Request Processing SLA",
            "task_en": "Within how many calendar days must a data controller process a GDPR Right to Erasure request?",
            "task_hi": "डेटा नियंत्रक को कितने दिनों के भीतर जीडीपीआर डेटा मिटाने (Right to Erasure) के अनुरोध को संसाधित करना होगा?",
            "task_te": "డేటా కంట్రోలర్ GDPR డేటా తొలగింపు (రైట్ టు ఎరేజర్) అభ్యర్థనను ఎన్ని రోజుల్లోగా పరిష్కరించాలి?",
            "task_teen": "GDPR Article 17 Right to Erasure deletion request ni enni days lo process cheyali?",
            "doc_en": "Under Article 17 of the General Data Protection Regulation (GDPR), individual data subjects possess the legal right to mandate the erasure of their personal data without undue delay. The statutory data controller must respond to and fulfill the erasure request within 30 calendar days of receiving verified identity documentation. In cases of complex enterprise data architectures, this timeframe may be extended by an additional 60 days.",
            "doc_hi": "जीडीपीआर के अनुच्छेद 17 के तहत, डेटा नियंत्रक को पहचान सत्यापन प्राप्त होने के 30 दिनों के भीतर व्यक्तिगत डेटा को मिटाने के अनुरोध को संसाधित करना होगा। जटिल प्रणालियों में, इसे अतिरिक्त 60 दिनों के लिए बढ़ाया जा सकता है।",
            "doc_te": "జనరల్ డేటా ప్రొటెక్షన్ రెగ్యులేషన్ (GDPR) ఆర్టికల్ 17 ప్రకారం, పౌరులు తమ వ్యక్తిగత డేటాను తొలగించాలని కోరే హక్కును కలిగి ఉన్నారు. సరైన గుర్తింపు పత్రాలు అందిన 30 క్యాలెండర్ రోజుల్లోగా డేటా కంట్రోలర్ ఆ సమాచారాన్ని శాశ్వతంగా తొలగించాలి. సంక్లిష్టమైన సాంకేతిక కారణాలు ఉంటే ఈ గడువును మరో 60 రోజుల వరకు పొడిగించవచ్చు.",
            "doc_teen": "GDPR Article 17 Right to Erasure prakaram data controller verified ID receive chesukunna 30 calendar days lopala personal data deletion process cheyali. Complex data architectures unte additional ga 60 days extension teesukovachu but notification ivvali."
        },
        {
            "topic": "Non-Disclosure Agreement Confidentiality Term",
            "task_en": "For how many years do trade secret confidentiality obligations survive under standard commercial NDAs?",
            "task_hi": "मानक वाणिज्यिक एनडीए के तहत व्यापार रहस्य की गोपनीयता दायित्व कितने वर्षों तक जीवित रहते हैं?",
            "task_te": "ప్రామాణిక వాణిజ్య ఒప్పందాల (NDA) కింద వ్యాపార రహస్యాల గోప్యతా కాలపరిమితి ఎన్ని సంవత్సరాలు ఉంటుంది?",
            "task_teen": "Commercial Non-Disclosure Agreement (NDA) lo trade secret obligations enni years survive avtayi?",
            "doc_en": "Standard corporate Non-Disclosure Agreements (NDAs) govern the exchange of proprietary technical and business information. General confidential business disclosures (such as pricing models and marketing briefs) remain protected for 3 years post-termination. However, statutory proprietary trade secrets, software source algorithms, and chemical formulations survive indefinitely for 5 years or as long as they qualify as trade secrets under law.",
            "doc_hi": "एनडीए के तहत सामान्य व्यावसायिक जानकारी 3 साल तक सुरक्षित रहती है। हालांकि, तकनीकी व्यापार रहस्य और स्रोत कोड 5 साल तक या जब तक वे कानून के तहत व्यापार रहस्य रहते हैं, तब तक सुरक्षित रहते हैं।",
            "doc_te": "కార్పొరేట్ నాన్-డిస్‌క్లోజర్ ఒప్పందాల (NDA) ప్రకారం సాధారణ వ్యాపార సమాచారం ఒప్పందం ముగిసిన తర్వాత 3 సంవత్సరాల పాటు గోప్యంగా ఉండాలి. అయితే, వాణిజ్య రహస్యాలు (ట్రేడ్ సీక్రెట్స్), సాఫ్ట్‌వేర్ సోర్స్ కోడ్ మరియు ప్రత్యేక ఫార్ములాల గోప్యత కనీసం 5 సంవత్సరాలు లేదా చట్టప్రకారం అవి రహస్యంగా ఉన్నంత కాలం కొనసాగుతుంది.",
            "doc_teen": "Standard NDA governance lo general confidential info 3 years protect avtundi. Kani proprietary trade secrets mariyu source code algorithms agreement terminate ayina 5 years kani statutory law prakaram trade secret ga unnantha varaku survive avtayi."
        },
        {
            "topic": "Open Source GPL v3 Reciprocal Licensing",
            "task_en": "What obligation does the GNU General Public License v3 impose on derivative software works?",
            "task_hi": "जीएनयू जनरल पब्लिक लाइसेंस v3 व्युत्पन्न सॉफ़्टवेयर कार्यों पर क्या दायित्व लगाता है?",
            "task_te": "GNU జనరల్ పబ్లిక్ లైసెన్స్ v3 సాఫ్ట్‌వేర్ ఆధారంగా తయారుచేసిన ఇతర ప్రాజెక్టులపై ఏ విధమైన నిబంధనలను విధిస్తుంది?",
            "task_teen": "GNU General Public License (GPL v3) derivative software works pai etuvanti conditions impose chesthundi?",
            "doc_en": "The GNU General Public License version 3 (GPL v3) operates as a strong copyleft reciprocal open source software license. Any proprietary codebase that statically links, incorporates, or creates derivative software incorporating GPL v3 licensed code must release its own complete source code under the identical GPL v3 terms when distributing the application binaries to external third parties.",
            "doc_hi": "जीपीएल v3 एक मजबूत कॉपीलेफ्ट लाइसेंस है। यदि कोई सॉफ्टवेयर जीपीएल v3 कोड का उपयोग करता है या जोड़ता है, तो बाहरी उपयोगकर्ताओं को सॉफ्टवेयर वितरित करते समय उसे अपना पूरा स्रोत कोड उसी जीपीएल v3 लाइसेंस के तहत जारी करना होगा।",
            "doc_te": "GNU జనరల్ పబ్లిక్ లైసెన్స్ v3 అనేది ఒక కఠినమైన కాపీలెఫ్ట్ ఓపెన్ సోర్స్ లైసెన్స్. GPL v3 లైసెన్స్ కలిగిన కోడ్‌ను ఉపయోగించి ఏదైనా కొత్త సాఫ్ట్‌వేర్ తయారుచేసినప్పుడు, ఆ సాఫ్ట్‌వేర్‌ను బయటి వారికి పంపిణీ చేసేటప్పుడు దాని పూర్తి సోర్స్ కోడ్‌ను కూడా అదే GPL v3 నిబంధనల ప్రకారం ఉచితంగా అందుబాటులో ఉంచాలి.",
            "doc_teen": "GPL v3 strong copyleft open source license ga act chesthundi. GPL v3 code ni link chesina derivative software create chesina, binaries external parties ki distribute chesetappudu entire application source code ni same GPL v3 terms kindha open release cheyadam mandatory."
        },
        {
            "topic": "Comparative Advertising Trademark Fair Use",
            "task_en": "Under what condition is a competitor's registered trademark permitted in comparative advertising?",
            "task_hi": "तुलनात्मक विज्ञापन में प्रतिस्पर्धी के पंजीकृत ट्रेडमार्क की अनुमति किस शर्त के तहत दी जाती है?",
            "task_te": "పోటీదారుల ట్రేడ్‌మార్క్‌ను ప్రకటనలలో ఉపయోగించడానికి అనుమతించబడే నిబంధన ఏమిటి?",
            "task_teen": "Comparative advertising lo competitor trademark fair use cheyadaniki legal condition enti?",
            "doc_en": "Statutory trademark law permits the limited nominative fair use of a competitor's registered trademark in comparative advertising, provided the usage is strictly truthful, non-misleading, and identifies specific verifiable metrics (such as performance benchmarks or retail price). The advertisement must not copy stylized graphic logos and must contain a prominent disclaimer acknowledging the third-party owner.",
            "doc_hi": "ट्रेडमार्क कानून तुलनात्मक विज्ञापन में प्रतिस्पर्धी के नाम के उपयोग की अनुमति देता है यदि तुलना सच्ची और गैर-भ्रामक हो। विज्ञापन में उनके लोगो की नकल नहीं की जानी चाहिए और एक स्पष्ट अस्वीकरण (Disclaimer) शामिल होना चाहिए।",
            "doc_te": "ట్రేడ్‌మార్క్ చట్టం ప్రకారం ప్రకటనలలో పోటీదారుల పేరును పోలికల కోసం ఉపయోగించవచ్చు, అయితే ఆ పోలిక నిజాయితీగా, తప్పుదోవ పట్టించకుండా మరియు నిర్దిష్ట వాస్తవాలపై ఆధారపడి ఉండాలి. వారి అధికారిక లోగోలను వాడకూడదు మరియు ఆ ట్రేడ్‌మార్క్ సంబంధిత సంస్థకు చెందినదని స్పష్టమైన నిరాకరణ (డిస్‌క్లైమర్) ప్రకటించాలి.",
            "doc_teen": "Comparative advertising lo competitor trademark nominative fair use allow avtundi if facts truthful mariyu non-misleading ga unte. Stylized graphic logos copy cheyakudadhu mariyu third-party ownership acknowledge chese clear disclaimer undali."
        },
        {
            "topic": "Mandatory Arbitration Clause in Terms of Service",
            "task_en": "How are consumer legal disputes resolved under the platform's mandatory arbitration agreement?",
            "task_hi": "मंच के अनिवार्य मध्यस्थता समझौते के तहत उपभोक्ता कानूनी विवादों का समाधान कैसे किया जाता है?",
            "task_te": "ప్లాట్‌ఫారమ్ యొక్క నిబంధనల ప్రకారం వినియోగదారుల వివాదాలు ఎలా పరిష్కరించబడతాయి?",
            "task_teen": "Terms of Service lo unna mandatory arbitration clause dwara disputes ela resolve avtayi?",
            "doc_en": "By accepting the enterprise platform Terms of Service, registered users agree that all contractual disputes or tort claims arising from service usage must be resolved through binding individual arbitration administered by the American Arbitration Association (AAA). Users explicitly waive rights to participate in class action lawsuits or public jury trials, and must initiate dispute proceedings within one year.",
            "doc_hi": "सेवा की शर्तों को स्वीकार करके, उपयोगकर्ता सहमत होते हैं कि सभी विवादों का समाधान मध्यस्थता संघ (AAA) द्वारा व्यक्तिगत मध्यस्थता के माध्यम से किया जाएगा। उपयोगकर्ता वर्ग-कार्रवाई मुकदमों (क्लास एक्शन) के अपने अधिकार को छोड़ देते हैं।",
            "doc_te": "ప్లాట్‌ఫారమ్ నిబంధనలను అంగీకరించడం ద్వారా వినియోగదారులు తమ వివాదాలన్నింటినీ న్యాయస్థానాల్లో కాకుండా ఆర్బిట్రేషన్ అసోసియేషన్ ద్వారా వ్యక్తిగతంగా పరిష్కరించుకోవడానికి అంగీకరిస్తారు. వినియోగదారులు సామూహిక వ్యాజ్యాలు (క్లాస్ యాక్షన్ సూట్స్) లేదా జ్యూరీ విచారణల హక్కును వదులుకుంటారు మరియు ఏడాదిలోపు వివాదాన్ని ప్రారంభించాలి.",
            "doc_teen": "Terms of Service accept chesina users all legal disputes ni individual binding arbitration dwara resolve chesukovadaniki agree avtharu. Class action lawsuits kani jury trials rights waive avtayi mariyu one year lopala arbitration proceedings file cheyali."
        },
        {
            "topic": "Website Cookie Consent Regulatory Compliance",
            "task_en": "Which category of cookies is exempt from mandatory prior user opt-in consent?",
            "task_hi": "उपयोगकर्ता की पूर्व सहमति के बिना कौन सी श्रेणी के कुकीज़ को छूट दी गई है?",
            "task_te": "ముందస్తు అనుమతి లేకుండా ఉపయోగించడానికి ఏ వర్గానికి చెందిన వెబ్‌సైట్ కుకీలకు మినహాయింపు ఉంది?",
            "task_teen": "Prior user opt-in consent lekunda direct ga use cheyadaniki exempt ayina cookie category enti?",
            "doc_en": "Under international ePrivacy regulations and European Data Protection Board directives, website operators must obtain active, unbundled opt-in consent prior to placing non-essential tracking cookies on visitor browsers. The sole category exempted from prior consent comprises 'Strictly Necessary Cookies'—defined as session identifiers and security tokens essential for fundamental website functioning and shopping cart persistence.",
            "doc_hi": "गोपनीयता नियमों के तहत, केवल 'सख्त रूप से आवश्यक कुकीज़' (Strictly Necessary Cookies) को पूर्व सहमति से छूट दी गई है, जो वेबसाइट के बुनियादी संचालन और कार्ट कार्यक्षमता के लिए आवश्यक हैं। विज्ञापन कुकीज़ के लिए सहमति आवश्यक है।",
            "doc_te": "అంతర్జాతీయ ప్రైవసీ నిబంధనల ప్రకారం వెబ్‌సైట్‌లు ట్రాకింగ్ కుకీలను ఉంచే ముందు యూజర్ అనుమతి తీసుకోవడం తప్పనిసరి. కేవలం 'అత్యంత అవసరమైన కుకీలు' (Strictly Necessary Cookies) అంటే వెబ్‌సైట్ ప్రాథమిక భద్రత, లాగిన్ సెషన్ మరియు షాపింగ్ కార్ట్ పనిచేయడానికి అవసరమైన వాటికి మాత్రమే ముందస్తు అనుమతి నుండి మినహాయింపు ఉంటుంది.",
            "doc_teen": "ePrivacy regulations prakaram non-essential tracking cookies ki prior opt-in consent compulsory. Kevalam 'Strictly Necessary Cookies' (session identifiers, security tokens, shopping cart persistence) ki matrame prior user consent nunchi exemption untundi."
        },
        {
            "topic": "Corporate Statutory Financial Audit Record Retention",
            "task_en": "How many years must audited corporate financial statements and tax ledgers be preserved?",
            "task_hi": "ऑडिट किए गए कॉर्पोरेट वित्तीय विवरणों और कर बहीखातों को कितने वर्षों तक संरक्षित किया जाना चाहिए?",
            "task_te": "ఆడిట్ చేయబడిన కార్పొరేట్ ఆర్థిక నివేదికలు మరియు పన్ను రికార్డులను ఎన్ని సంవత్సరాలు భద్రపరచాలి?",
            "task_teen": "Audited corporate financial statements mariyu tax ledgers enni years preserve cheyali?",
            "doc_en": "Statutory corporate accounting standards and federal revenue codes require incorporated commercial enterprises to retain audited annual balance sheets, general transaction ledgers, and supported tax return schedules for a minimum statutory retention period of 7 years following filing date. Records involving pending governmental litigation must be retained indefinitely until formal legal closure.",
            "doc_hi": "कॉर्पोरेट लेखा मानकों के तहत कंपनियों को ऑडिट की गई वार्षिक बैलेंस शीट और टैक्स रिकॉर्ड को फाइल करने की तारीख से कम से कम 7 साल तक सुरक्षित रखना आवश्यक है। कानूनी विवादों से जुड़े रिकॉर्ड को विवाद समाप्त होने तक रखना होगा।",
            "doc_te": "కార్పొరేట్ అకౌంటింగ్ నిబంధనల ప్రకారం కంపెనీలు తమ ఆడిట్ చేయబడిన వార్షిక నివేదికలు, లావాదేవీల లెడ్జర్లు మరియు పన్ను రిటర్నుల పత్రాలను సమర్పించిన తేదీ నుండి కనీసం 7 సంవత్సరాల పాటు భద్రపరచాలి. కోర్టు కేసులు ఉన్న రికార్డులను వివాదం పరిష్కారమయ్యే వరకు శాశ్వతంగా ఉంచాలి.",
            "doc_teen": "Corporate accounting compliance prakaram audited balance sheets, general ledgers mariyu tax return filings minimum 7 years statutory period varaku preserve cheyali. Litigation unna records legal dispute close ayye varaku retain cheyadam mandatory."
        },
        {
            "topic": "Contractual Breach Notice and Cure Period",
            "task_en": "How many days notice must be provided to cure a material breach of contract prior to termination?",
            "task_hi": "अनुबंध समाप्त करने से पहले सामग्री उल्लंघन को ठीक करने के लिए कितने दिनों का नोटिस दिया जाना चाहिए?",
            "task_te": "ఒప్పందాన్ని రద్దు చేయడానికి ముందు లోపాన్ని సరిదిద్దుకోవడానికి ఎన్ని రోజుల నోటీసు ఇవ్వాలి?",
            "task_teen": "Contractual material breach cure cheyadaniki notice period enni days ivvali?",
            "doc_en": "Commercial procurement contracts stipulate standard default remedies in the event of contractual non-performance. Before an aggrieved party can lawfully terminate an agreement for cause, they must serve formal written notice specifying the exact nature of the material default. The defaulting counterparty is granted a mandatory 30-day cure period from notice receipt to rectify the operational deficiency.",
            "doc_hi": "वाणिज्यिक अनुबंधों के तहत, किसी समझौते को समाप्त करने से पहले, पीड़ित पक्ष को लिखित नोटिस देना होगा। उल्लंघन करने वाले पक्ष को गलती सुधारने के लिए नोटिस मिलने से 30 दिनों का समय दिया जाता है।",
            "doc_te": "వాణిజ్య ఒప్పందాల ప్రకారం ఏదైనా ఒక పక్షం ఒప్పంద నిబంధనలను పాటించకపోతే, ఒప్పందాన్ని రద్దు చేసే ముందు ఎదుటి పక్షానికి లిఖితపూర్వక నోటీసు ఇవ్వాలి. లోపాన్ని సరిదిద్దుకోవడానికి (క్యూర్ పీరియడ్) నోటీసు అందిన తేదీ నుండి తప్పనిసరిగా 30 రోజుల గడువు ఇవ్వాల్సి ఉంటుంది.",
            "doc_teen": "Commercial contracts lo termination for cause chese munde formal written notice ivvali specifying the material default. Defaulting party ki operational deficiency rectify cheyadaniki notice receipt nunchi mandatory 30-day cure period untundi."
        },
        {
            "topic": "Corporate Whistleblower Anti-Retaliation Protections",
            "task_en": "What legal safeguards protect corporate employees reporting regulatory wrongdoing?",
            "task_hi": "नियामक गलतियों की रिपोर्ट करने वाले कॉर्पोरेट कर्मचारियों को क्या कानूनी सुरक्षा प्राप्त है?",
            "task_te": "సంస్థలో అక్రమాలను నివేదించే విజిల్‌బ్లోయర్ ఉద్యోగులకు ఏ విధమైన చట్టపరమైన రక్షణలు ఉంటాయి?",
            "task_teen": "Corporate regulatory fraud report chese whistleblower employees ki etuvanti legal protections untayi?",
            "doc_en": "Statutory whistleblower protection frameworks guarantee absolute confidentiality for employees reporting suspected securities fraud, environmental violations, or accounting discrepancies via the independent ethics hotline. Company bylaws and federal statutes strictly prohibit employer retaliation, including termination, demotion, harassment, or compensation reduction, subjecting violators to criminal prosecution.",
            "doc_hi": "कानून वित्तीय धोखाधड़ी या नियमों के उल्लंघन की रिपोर्ट करने वाले कर्मचारियों के लिए पूर्ण गोपनीयता की गारंटी देता है। कानून प्रतिशोध, बर्खास्तगी या उत्पीड़न को प्रतिबंधित करता है और ऐसा करने वालों पर आपराधिक मुकदमा चलाया जा सकता है।",
            "doc_te": "విజిల్‌బ్లోయర్ రక్షణ చట్టాల ప్రకారం సంస్థలో జరిగే ఆర్థిక అవకతవకలు లేదా మోసాలను ఎథిక్స్ హాట్‌లైన్ ద్వారా నివేదించే ఉద్యోగుల వివరాలు పూర్తిగా గోప్యంగా ఉంచబడతాయి. అటువంటి ఉద్యోగులపై ఉద్యోగ తొలగింపు, హోదా తగ్గించడం లేదా వేధింపుల వంటి ఎలాంటి ప్రతీకార చర్యలు తీసుకోకూడదు, ఉల్లంఘిస్తే క్రిమినల్ కేసులు నమోదు చేస్తారు.",
            "doc_teen": "Whistleblower protection framework ethics hotline dwara regulatory fraud report chese employees ki absolute confidentiality guarantee chesthundi. Employer retaliation (termination, demotion, harassment) strictly illegal mariyu violators criminal prosecution face chestharu."
        },
        {
            "topic": "Dual-Use Cryptographic Software Export Controls",
            "task_en": "What regulatory license is required to export proprietary symmetric encryption software exceeding 64 bits?",
            "task_hi": "64 बिट से अधिक के सममित एन्क्रिप्शन सॉफ़्टवेयर को निर्यात करने के लिए किस विनियामक लाइसेंस की आवश्यकता है?",
            "task_te": "64 బిట్లకు మించిన ఎన్‌క్రిప్షన్ సాఫ్ట్‌వేర్‌ను విదేశాలకు ఎగుమతి చేయడానికి ఏ లైసెన్స్ అవసరం?",
            "task_teen": "64-bit encryption exceed ayye cryptographic software export cheyadaniki regulatory license emiti?",
            "doc_en": "Under Export Administration Regulations (EAR) and international Wassenaar Arrangement guidelines, proprietary commercial software implementing symmetric cryptographic key lengths exceeding 64 bits is classified as a dual-use controlled commodity under Export Control Classification Number (ECCN) 5D002. Re-exporting this technology to restricted destinations requires an official commerce export license.",
            "doc_hi": "निर्यात नियमों (EAR) के तहत, 64 बिट से अधिक के सिमेट्रिक एन्क्रिप्शन सॉफ़्टवेयर को दोहरे उपयोग वाली वस्तु माना जाता है। इसे प्रतिबंधित देशों में निर्यात करने के लिए वाणिज्य विभाग से आधिकारिक निर्यात लाइसेंस की आवश्यकता होती है।",
            "doc_te": "అంతర్జాతీయ ఎగుమతి నిబంధనల (EAR) ప్రకారం 64 బిట్లకు మించిన సమరూప (సిమెట్రిక్) ఎన్‌క్రిప్షన్ కలిగిన సాఫ్ట్‌వేర్ ద్వంద్వ-వినియోగ వస్తువుగా వర్గీకరించబడింది. ఈ సాంకేతికతను ఇతర దేశాలకు ఎగుమతి చేయడానికి లేదా బదిలీ చేయడానికి వాణిజ్య శాఖ నుండి అధికారిక ఎగుమతి లైసెన్స్ తీసుకోవడం తప్పనిసరి.",
            "doc_teen": "Export Administration Regulations (EAR) prakaram 64-bit kante ekkuva unna symmetric encryption software dual-use controlled commodity ga classify avtundi. Ee cryptographic tools restricted countries ki re-export cheyali ante official commerce export license kavali."
        }
    ]
}

# Domain 10: Customer Service & IT Helpdesk (S091 - S100)
D10 = {
    "domain": "customer_support",
    "scenarios": [
        {
            "topic": "Tier 1 Priority Support Ticket Response SLA",
            "task_en": "What is the guaranteed initial engineer response time for High-Priority technical support tickets?",
            "task_hi": "उच्च प्राथमिकता वाले तकनीकी सहायता टिकटों के लिए शुरुआती प्रतिक्रिया समय क्या है?",
            "task_te": "హై-ప్రయారిటీ సాంకేతిక మద్దతు టికెట్లకు నిర్దేశించిన ప్రారంభ స్పందన సమయం (SLA) ఎంత?",
            "task_teen": "High-Priority technical support tickets ki guaranteed first response SLA entha?",
            "doc_en": "Enterprise customer service level agreements (SLAs) delineate explicit response and resolution timeframes based on ticket priority. Technical support cases categorized as High-Priority (impacting core business operations without total system failure) require a certified support engineer to provide an initial diagnostic response within 60 minutes of ticket submission, 24 hours a day, 7 days a week.",
            "doc_hi": "उच्च प्राथमिकता वाले तकनीकी मामलों के लिए एक प्रमाणित इंजीनियर को टिकट जमा करने के 60 मिनट के भीतर शुरुआती निदान प्रदान करना आवश्यक है। यह सेवा सप्ताह के सातों दिन 24 घंटे उपलब्ध है।",
            "doc_te": "కార్పొరేట్ సర్వీస్ లెవల్ అగ్రిమెంట్స్ (SLA) ప్రకారం హై-ప్రయారిటీ సాంకేతిక సమస్యలకు (సంస్థ పనులకు ఆటంకం కలిగించేవి) టికెట్ నమోదు చేసిన 60 నిమిషాల లోపు సర్టిఫైడ్ ఇంజనీర్ మొదటి స్పందన మరియు ప్రాథమిక విశ్లేషణను అందించాలి. ఈ సేవ వారానికి 7 రోజులు 24 గంటలు అందుబాటులో ఉంటుంది.",
            "doc_teen": "Enterprise SLAs prakaram High-Priority support tickets (business impact unna cases) ki support engineer 60 minutes lopala initial diagnostic response ivvali. Ee SLA 24/7 round the clock applicable ga untundi."
        },
        {
            "topic": "Customer Satisfaction CSAT Survey Trigger Timing",
            "task_en": "How many hours after ticket resolution is an automated CSAT satisfaction survey dispatched?",
            "task_hi": "टिकट समाधान के कितने घंटे बाद स्वचालित संतुष्टि सर्वेक्षण (CSAT) भेजा जाता है?",
            "task_te": "సమస్య పరిష్కారమైన ఎన్ని గంటల తర్వాత కస్టమర్ సంతృప్తి సర్వే (CSAT) పంపబడుతుంది?",
            "task_teen": "Support ticket resolve ayina enni hours tharuvatha automated CSAT survey send chestharu?",
            "doc_en": "To objectively evaluate helpdesk service quality, the support automation ticketing platform schedules a Customer Satisfaction (CSAT) survey exactly 24 hours following confirmed ticket closure. This window allows users to confirm issue resolution before rating their experience on a 1-to-5 star scale. CSAT scores below 3 stars trigger an automated management follow-up review within 48 hours.",
            "doc_hi": "टिकट बंद होने के ठीक 24 घंटे बाद एक ग्राहक संतुष्टि (CSAT) सर्वेक्षण भेजा जाता है। इससे उपयोगकर्ताओं को अनुभव को 1-से-5 स्टार पैमाने पर आंकने की अनुमति मिलती है। 3 स्टार से कम रेटिंग पर समीक्षा की जाती है।",
            "doc_te": "సేవా నాణ్యతను తెలుసుకోవడానికి టికెట్ పరిష్కారమై క్లోజ్ అయిన ఖచ్చితంగా 24 గంటల తర్వాత ఆటోమేటెడ్ కస్టమర్ సంతృప్తి (CSAT) సర్వే పంపబడుతుంది. కస్టమర్లు తమ అనుభవాన్ని 1 నుండి 5 నక్షత్రాల స్కేల్‌లో రేట్ చేయవచ్చు. 3 స్టార్స్ కంటే తక్కువ రేటింగ్ వస్తే మేనేజర్లు 48 గంటల్లో కస్టమర్‌ను సంప్రదించాలి.",
            "doc_teen": "Service quality evaluate cheyadaniki ticket close ayina exactly 24 hours tharuvatha CSAT survey trigger avtundi. Users issue resolution check chesukoni 1 to 5 star rating istharu. Rating below 3 stars unte management team 48 hours lo follow-up chesthundi."
        },
        {
            "topic": "Corporate Laptop Replacement Courier Turnaround",
            "task_en": "What is the standard turnaround time for shipping replacement hardware for malfunctioning corporate laptops?",
            "task_hi": "खराब लैपटॉप के लिए हार्डवेयर बदलने का मानक समय क्या है?",
            "task_te": "పాడైన కంపెనీ ల్యాప్‌టాప్‌ను మార్చి కొత్తది పంపడానికి ఎంత సమయం పడుతుంది?",
            "task_teen": "Corporate laptop defective ayithe replacement hardware dispatch turnaround time entha?",
            "doc_en": "When remote corporate personnel report verified hardware failure (such as persistent motherboard faults or unbootable drives), the IT logistics asset desk dispatches a pre-configured, encrypted corporate replacement laptop via priority express courier within 2 business days. The employee must return the malfunctioning hardware in the prepaid return packaging within 14 calendar days.",
            "doc_hi": "हार्डवेयर की विफलता की पुष्टि होने पर, आईटी टीम 2 कार्य दिवसों के भीतर एक पूर्व-कॉन्फ़िगर किया गया नया लैपटॉप भेजती है। कर्मचारी को 14 दिनों के भीतर पुराने उपकरण वापस करने होंगे।",
            "doc_te": "ఉద్యోగి ల్యాప్‌టాప్‌లో హార్డ్‌వేర్ లోపం నిర్ధారణ అయినప్పుడు, ఐటీ విభాగం అన్ని సాఫ్ట్‌వేర్లతో సిద్ధం చేసిన కొత్త ల్యాప్‌టాప్‌ను ఎక్స్‌ప్రెస్ కొరియర్ ద్వారా 2 పని దినాల్లోగా పంపిస్తుంది. ఉద్యోగి పాత పాడైన ల్యాప్‌టాప్‌ను 14 రోజుల్లోగా కంపెనీ అందించిన బాక్స్‌లో తిరిగి పంపించాలి.",
            "doc_teen": "Remote staff hardware failure confirm ayithe IT asset desk encrypted replacement laptop ni priority courier dwara 2 business days lo dispatch chesthundi. Employee defective unit ni prepaid packaging lo 14 calendar days lo return pampali."
        },
        {
            "topic": "Knowledge Base Documentation Review Cadence",
            "task_en": "How frequently must internal IT knowledge base articles be reviewed and recertified?",
            "task_hi": "आंतरिक आईटी ज्ञानकोष लेखों की कितनी बार समीक्षा और पुनः प्रमाणन किया जाना चाहिए?",
            "task_te": "ఐటీ విజ్ఞాన సర్వస్వంలోని (నాలెడ్జ్ బేస్) డాక్యుమెంట్లను ఎంత కాలానికి ఒకసారి సమీక్షించి అప్‌డేట్ చేయాలి?",
            "task_teen": "Internal IT knowledge base articles ni entha frequency tho review mariyu recertify cheyali?",
            "doc_en": "To maintain procedural accuracy, IT service management policies dictate that all published knowledge base articles, standard operating procedures, and customer troubleshooting manuals undergo mandatory biannual reviews every 6 months. Subject matter experts must test procedural instructions, update outdated screenshots, and recertify technical validity.",
            "doc_hi": "सटीकता बनाए रखने के लिए, सभी प्रकाशित ज्ञानकोष लेखों और समस्या निवारण मैनुअल की हर 6 महीने में समीक्षा की जानी चाहिए। विशेषज्ञों को निर्देशों का परीक्षण और वैधता का नवीनीकरण करना होगा।",
            "doc_te": "సమాచార ఖచ్చితత్వం కోసం అన్ని ఐటీ నాలెడ్జ్ బేస్ వ్యాసాలు మరియు ట్రబుల్ షూటింగ్ గైడ్‌లను ప్రతి 6 నెలలకు ఒకసారి సమీక్షించి పునఃధృవీకరించాలి. నిపుణులు ప్రక్రియలను పరీక్షించి, స్క్రీన్‌షాట్‌లను అప్‌డేట్ చేసి తాజా మార్పులను పొందుపరచాలి.",
            "doc_teen": "Procedural accuracy kosam internal knowledge base articles mariyu troubleshooting manuals ni prathi 6 months ki mandatory ga review cheyali. Subject matter experts technical instructions verify chesi validity recertify chestharu."
        },
        {
            "topic": "Live Support Chat Inactivity Disconnect Timeout",
            "task_en": "How many minutes of customer silence trigger an automated disconnect on support live chats?",
            "task_hi": "ग्राहक की चुप्पी के कितने मिनट बाद लाइव चैट अपने आप डिस्कनेक्ट हो जाती है?",
            "task_te": "కస్టమర్ నుండి స్పందన లేకపోతే ఎన్ని నిమిషాల తర్వాత లైవ్ చాట్ ఆటోమేటిక్‌గా ముగుస్తుంది?",
            "task_teen": "Live customer support chat lo customer silence unte enni minutes lo auto disconnect avtundi?",
            "doc_en": "Real-time web chat support platforms employ automated idle timers to maintain routing queue capacity. If an active customer does not transmit a message for 3 continuous minutes, an automated reminder prompt is presented. If customer silence persists for an additional 2 minutes (5 minutes total inactivity), the chat session closes automatically with a transcript emailed to the user.",
            "doc_hi": "यदि ग्राहक 3 मिनट तक कोई संदेश नहीं भेजता है, तो एक रिमाइंडर भेजा जाता है। यदि 2 और मिनट (कुल 5 मिनट) तक कोई प्रतिक्रिया नहीं होती है, तो चैट सत्र स्वचालित रूप से समाप्त हो जाता है।",
            "doc_te": "కస్టమర్ సర్వీస్ లైవ్ చాట్ విధానంలో నిరంతరంగా 3 నిమిషాల పాటు కస్టమర్ నుండి ఎలాంటి సందేశం రాకపోతే రిమైండర్ వస్తుంది. మరో 2 నిమిషాలు (మొత్తం 5 నిమిషాల నిష్క్రియాత్మకత) గడిచినా సమాధానం లేకపోతే చాట్ ఆటోమేటిక్‌గా ముగిసిపోతుంది మరియు వివరాలు ఇమెయిల్‌కు పంపబడతాయి.",
            "doc_teen": "Live chat platform lo 3 minutes continuous silence unte reminder alert vastundi. Another 2 minutes (total 5 minutes inactivity) respond avvakapothe session automatically disconnect ayyi chat transcript user email ki pampistharu."
        },
        {
            "topic": "Tier 2 Engineering Escalation Criteria",
            "task_en": "When does a customer support ticket escalate from Tier 1 helpdesk to Tier 2 engineering?",
            "task_hi": "ग्राहक सहायता टिकट टियर 1 से टियर 2 इंजीनियरिंग तक कब बढ़ता है?",
            "task_te": "కస్టమర్ సపోర్ట్ టికెట్ టైర్ 1 నుండి టైర్ 2 ఇంజనీరింగ్ బృందానికి ఎప్పుడు బదిలీ అవుతుంది?",
            "task_teen": "Support ticket Tier 1 nunchi Tier 2 engineering ki escalate chese criteria emiti?",
            "doc_en": "Frontline Tier 1 customer representatives must escalate a technical case to Tier 2 specialized engineering under strict conditions: whenever a software bug cannot be resolved using documented knowledge base procedures within 2 failed customer attempts, or when the underlying issue indicates database corruption, code defects, or regional infrastructure downtime.",
            "doc_hi": "टियर 1 प्रतिनिधि टिकट को टियर 2 इंजीनियरिंग को तब सौंपते हैं जब 2 असफल प्रयासों के बाद भी समस्या का समाधान नहीं होता है, या जब समस्या कोड दोष या डेटाबेस में खराबी से जुड़ी हो।",
            "doc_te": "డాక్యుమెంట్లలో పేర్కొన్న పద్ధతుల ద్వారా రెండు ప్రయత్నాల్లో సమస్య పరిష్కారం కానప్పుడు లేదా సమస్య సాఫ్ట్‌వేర్ లోపాలు, డేటాబేస్ సమస్యలు మరియు సర్వర్ డౌన్‌టైమ్‌కు సంబంధించినదైతే టైర్ 1 ప్రతినిధులు ఆ టికెట్‌ను వెంటనే టైర్ 2 ఇంజనీరింగ్ బృందానికి బదిలీ చేస్తారు.",
            "doc_teen": "Documented procedures tho 2 failed attempts lo issue resolve avvakapothe, kani bug database corruption mariyu code defects ki related ayithe Tier 1 agents ticket ni Tier 2 engineering ki escalate chestharu."
        },
        {
            "topic": "Frontline Support Refund Authorization Threshold",
            "task_en": "What is the maximum dollar refund a frontline support agent can authorize without manager sign-off?",
            "task_hi": "प्रबंधक की मंजूरी के बिना एक फ्रंटलाइन सहायता एजेंट अधिकतम कितने डॉलर का रिफंड दे सकता है?",
            "task_te": "మేనేజర్ ఆమోదం అవసరం లేకుండా సాధారణ సపోర్ట్ ఏజెంట్ గరిష్టంగా ఎంత మొత్తం రీఫండ్‌ను మంజూరు చేయవచ్చు?",
            "task_teen": "Frontline support representative manager approval lekunda maximum entha refund authorize cheyavachu?",
            "doc_en": "To expedite customer dispute resolution, certified frontline Tier 1 support representatives are granted discretionary financial authorization to issue courtesy credits or order refunds up to a maximum limit of $50 per customer incident without requiring supervisory managerial approval. Any refund request exceeding $50 must be routed through the department supervisor queue.",
            "doc_hi": "विवादों को तेजी से हल करने के लिए, फ्रंटलाइन एजेंटों को पर्यवेक्षक की मंजूरी के बिना प्रति घटना अधिकतम $50 तक का रिफंड जारी करने का अधिकार है। $50 से अधिक के रिफंड के लिए प्रबंधक की मंजूरी आवश्यक है।",
            "doc_te": "వినియోగదారుల సమస్యలను త్వరగా పరిష్కరించడానికి టైర్ 1 సపోర్ట్ ఏజెంట్లకు సూపర్వైజర్ ఆమోదం లేకుండా ఒక్కో సమస్యకు గరిష్టంగా $50 వరకు రీఫండ్ మంజూరు చేసే అధికారం ఉంటుంది. $50 కంటే ఎక్కువ మొత్తాన్ని వాపసు చేయాలంటే తప్పనిసరిగా విభాగ మేనేజర్ అనుమతి తీసుకోవాలి.",
            "doc_teen": "Disputes fast ga settle cheyadaniki Tier 1 support agents ki single incident ki up to $50 refund manager approval lekunda authorize chese authority untundi. $50 threshold exceed ayithe supervisor queue ki route cheyali."
        },
        {
            "topic": "IT Self-Service Password Reset Authentication",
            "task_en": "What authentication factors are required to reset an enterprise domain password via self-service?",
            "task_hi": "सेल्फ-सर्विस के माध्यम से पासवर्ड रीसेट करने के लिए किन प्रमाणीकरण कारकों की आवश्यकता होती है?",
            "task_te": "సెల్ఫ్ సర్వీస్ పోర్టల్ ద్వారా డొమైన్ పాస్‌వర్డ్‌ను రీసెట్ చేయడానికి ఏ వివరాలు అవసరం?",
            "task_teen": "Self-service password reset portal lo domain password reset cheyadaniki auth steps emiti?",
            "doc_en": "Employees locked out of corporate domain accounts may utilize the IT Self-Service Password Reset (SSPR) portal. Identity verification requires two independent authentication factors: entry of a dynamic 6-digit one-time passcode transmitted to a pre-registered mobile number, followed by successful answer validation for two pre-selected personal security questions.",
            "doc_hi": "पासवर्ड रीसेट करने के लिए दो प्रमाणीकरण कारकों की आवश्यकता होती है: मोबाइल नंबर पर भेजा गया 6-अंकीय ओटीपी और दो पूर्व-चयनित व्यक्तिगत सुरक्षा प्रश्नों के सही उत्तर।",
            "doc_te": "ఖాతా లాక్ అయిన ఉద్యోగులు సెల్ఫ్ సర్వీస్ పోర్టల్ ద్వారా పాస్‌వర్డ్ మార్చుకోవచ్చు. దీని కోసం రెండు పద్ధతులు అవసరం: మొబైల్ నంబర్‌కు వచ్చే 6 అంకెల OTP ని నమోదు చేయాలి మరియు గతంలో ఎంచుకున్న రెండు వ్యక్తిగత భద్రతా ప్రశ్నలకు సరైన సమాధానాలు ఇవ్వాలి.",
            "doc_teen": "Self-Service Password Reset (SSPR) portal lo two-factor verification kavali: registered mobile number ki vachina 6-digit SMS OTP enter cheyali mariyu two pre-selected security questions ki correct answers ivvali."
        },
        {
            "topic": "After-Hours Critical P1 Incident On-Call Routing",
            "task_en": "How are after-hours critical P1 infrastructure outages routed to the engineering on-call rotation?",
            "task_hi": "कार्यालय समय के बाद के महत्वपूर्ण P1 आउटेज को ऑन-कॉल इंजीनियरिंग टीम को कैसे भेजा जाता है?",
            "task_te": "ఆఫీస్ పనివేళల తర్వాత సంభవించే అత్యవసర సర్వర్ సమస్యలను ఆన్-కాల్ ఇంజనీర్లకు ఎలా చేరవేస్తారు?",
            "task_teen": "After-hours P1 critical outage alerts on-call engineering roster ki ela route avtayi?",
            "doc_en": "During non-business hours, holidays, and weekends, automated infrastructure health monitors and high-priority customer alerts route through PagerDuty. If an automated P1 critical outage alert is not acknowledged by the designated primary on-call site reliability engineer within 10 minutes, the paging schedule automatically escalates via phone call to the secondary backup engineer.",
            "doc_hi": "कार्यालय समय के बाद गंभीर P1 अलर्ट PagerDuty के माध्यम से भेजे जाते हैं। यदि प्राथमिक ऑन-कॉल इंजीनियर 10 मिनट के भीतर जवाब नहीं देता है, तो अलर्ट स्वचालित रूप से फोन कॉल के माध्यम से द्वितीयक बैकअप इंजीनियर को भेज दिया जाता है।",
            "doc_te": "పనివేళలు ముగిసిన తర్వాత లేదా సెలవు దినాల్లో అత్యవసర P1 సర్వర్ సమస్యలు వస్తే PagerDuty ద్వారా అలర్ట్‌లు వెళ్తాయి. డ్యూటీలో ఉన్న ప్రైమరీ ఇంజనీర్ 10 నిమిషాల్లో స్పందించకపోతే, సిస్టమ్ ఆటోమేటిక్‌గా సెకండరీ బ్యాకప్ ఇంజనీర్‌కు ఫోన్ కాల్ చేసి అప్రమత్తం చేస్తుంది.",
            "doc_teen": "Non-business hours lo critical P1 alerts PagerDuty dwara route avtayi. Primary on-call engineer 10 minutes lo alert acknowledge cheyakapothe automated escalation secondary backup engineer ki automated phone call dwara trigger avtundi."
        },
        {
            "topic": "Customer Feature Request Feedback Roadmap Triage",
            "task_en": "How frequently does product management review customer-submitted feature suggestions?",
            "task_hi": "उत्पाद प्रबंधन कितनी बार ग्राहकों द्वारा प्रस्तुत सुविधा सुझावों की समीक्षा करता है?",
            "task_te": "కస్టమర్లు సమర్పించే ఫీచర్ అభ్యర్థనలను ప్రోడక్ట్ మేనేజ్‌మెంట్ ఎంత కాలానికి ఒకసారి సమీక్షిస్తుంది?",
            "task_teen": "Customer feature requests mariyu feedback portal submissions product team enni days ki review chesthundi?",
            "doc_en": "Customer feature enhancements submitted via the community feedback portal undergo structured monthly triage by the product management team. Suggestions achieving at least 50 community upvotes are evaluated against quarterly product roadmap priorities. Authors of accepted feature proposals receive automated status notifications when their request transitions from 'Under Review' to 'Scheduled'.",
            "doc_hi": "ग्राहक सुझावों की उत्पाद प्रबंधन टीम द्वारा हर महीने समीक्षा की जाती है। कम से कम 50 वोट पाने वाले सुझावों का मूल्यांकन किया जाता है और स्थिति बदलने पर उपयोगकर्ताओं को सूचित किया जाता है।",
            "doc_te": "కమ్యూనిటీ పోర్టల్ ద్వారా కస్టమర్లు ఇచ్చే కొత్త ఫీచర్ల సలహాలను ప్రోడక్ట్ మేనేజ్‌మెంట్ బృందం ప్రతి నెలా సమీక్షిస్తుంది. కనీసం 50 మంది మద్దతు తెలిపిన (అప్‌వోట్స్) సలహాలను త్రైమాసిక ప్రణాళికల్లో చేరుస్తారు మరియు వాటి స్థితి మారినప్పుడు కస్టమర్‌కు ఇమెయిల్ అందుతుంది.",
            "doc_teen": "Feedback portal lo submit chesina customer feature requests ni product management monthly triage chesthundi. At least 50 community upvotes unna suggestions ni roadmap priorities tho evaluate chesi status 'Scheduled' ga update chestharu."
        }
    ]
}

BUILDER2_DOMAINS = [D6, D7, D8, D9, D10]
