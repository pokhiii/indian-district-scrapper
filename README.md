# Indian State District Scraper

## Motivation

**Why I created this project?**

All of this started when I had to put a couple of dropdowns in a mobile app I was working: `State` and `District`.

The State dropdown meant to have a list of all the Indian states. The District dropdown meant to have a list of all the districts in the State selected in the first dropdown.

I wanted a JavaScript object/array but I was too frustated to find that a lot of the gists that exists on the Internet were outdated (eg. [1](https://github.com/sab99r/Indian-States-And-Districts/blob/master/states-and-districts.json)). I looked at India's [Open Government Data (OGD)](https://data.gov.in/) platform but couldn't find a simple API that would give me what I need.

Then I came across India's [Integrated Government Online Directory](https://igod.gov.in/sg/district/states) and there I found what I needed...with one catch: the information was present only in the webpage (hence HTML). I checked if there are `Fetch/XHR` requests happening to fetch data from a backend service but alas! nothing was in there. Then I decided to write this scraper!

## Installation

### Prerequisites

1. Docker
2. Docker Compose

### Steps

1. Clone the project
   ```sh
   git clone https://github.com/pokhiii/indian-district-scrapper.git
   ```
2. Change directory
   ```sh
   cd indian-district-scrapper
   ```
3. Start scraping
   ```
   docker compose up
   ```

> _Note: Scraping will take some time ~1 minute because it actually visiting each state's page one by one. So don't get confused after firing `docker compose up`; go for a walk or something while the script is doing it's magic._

## Results

### State List

```json
[
  {
    "name": "Andaman and Nicobar Islands",
    "code": "AN"
  },
  {
    "name": "Andhra Pradesh",
    "code": "AP"
  },
  {
    "name": "Arunachal Pradesh",
    "code": "AR"
  },
  {
    "name": "Assam",
    "code": "AS"
  },
  {
    "name": "Bihar",
    "code": "BR"
  },
  {
    "name": "Chandigarh",
    "code": "CH"
  },
  {
    "name": "Chhattisgarh",
    "code": "CG"
  },
  {
    "name": "Dadra and Nagar Haveli and Daman and Diu",
    "code": "ND"
  },
  {
    "name": "Delhi",
    "code": "DL"
  },
  {
    "name": "Goa",
    "code": "GA"
  },
  {
    "name": "Gujarat",
    "code": "GJ"
  },
  {
    "name": "Haryana",
    "code": "HR"
  },
  {
    "name": "Himachal Pradesh",
    "code": "HP"
  },
  {
    "name": "Jammu and Kashmir",
    "code": "JK"
  },
  {
    "name": "Jharkhand",
    "code": "JH"
  },
  {
    "name": "Karnataka",
    "code": "KA"
  },
  {
    "name": "Kerala",
    "code": "KL"
  },
  {
    "name": "Ladakh",
    "code": "LA"
  },
  {
    "name": "Lakshadweep",
    "code": "LD"
  },
  {
    "name": "Madhya Pradesh",
    "code": "MP"
  },
  {
    "name": "Maharashtra",
    "code": "MH"
  },
  {
    "name": "Manipur",
    "code": "MN"
  },
  {
    "name": "Meghalaya",
    "code": "ML"
  },
  {
    "name": "Mizoram",
    "code": "MZ"
  },
  {
    "name": "Nagaland",
    "code": "NL"
  },
  {
    "name": "Odisha",
    "code": "OD"
  },
  {
    "name": "Puducherry",
    "code": "PY"
  },
  {
    "name": "Punjab",
    "code": "PB"
  },
  {
    "name": "Rajasthan",
    "code": "RJ"
  },
  {
    "name": "Sikkim",
    "code": "SK"
  },
  {
    "name": "Tamil Nadu",
    "code": "TN"
  },
  {
    "name": "Telangana",
    "code": "TS"
  },
  {
    "name": "Tripura",
    "code": "TR"
  },
  {
    "name": "Uttar Pradesh",
    "code": "UP"
  },
  {
    "name": "Uttarakhand",
    "code": "UK"
  },
  {
    "name": "West Bengal",
    "code": "WB"
  }
]
```

### State District List

```json
{
  "AN": ["Nicobars", "North And Middle Andaman", "South Andamans"],
  "AP": [
    "Alluri Sitharama Raju",
    "Anakapalli",
    "Ananthapuramu",
    "Annamayya",
    "Bapatla",
    "Chittoor",
    "Dr. B.R. Ambedkar Konaseema",
    "East Godavari",
    "Eluru",
    "Guntur",
    "Kakinada",
    "Krishna",
    "Kurnool",
    "Nandyal",
    "Ntr",
    "Palnadu",
    "Parvathipuram Manyam",
    "Prakasam",
    "Sri Potti Sriramulu Nellore",
    "Sri Sathya Sai",
    "Srikakulam",
    "Tirupati",
    "Visakhapatnam",
    "Vizianagaram",
    "West Godavari"
  ],
  "AR": [
    "Anjaw",
    "Changlang",
    "Dibang Valley",
    "East Kameng",
    "East Siang",
    "Sub Districts",
    "Kra Daadi",
    "Kurung Kumey",
    "Sub Districts",
    "Lohit",
    "Longding",
    "Lower Dibang Valley",
    "Sub Districts",
    "Lower Subansiri",
    "Namsai",
    "Sub Districts",
    "Papum Pare",
    "Shi Yomi",
    "Siang",
    "Tawang",
    "Tirap",
    "Upper Siang",
    "Upper Subansiri",
    "West Kameng",
    "West Siang"
  ],
  "AS": [
    "Bajali",
    "Baksa",
    "Barpeta",
    "Biswanath",
    "Bongaigaon",
    "Cachar",
    "Charaideo",
    "Chirang",
    "Darrang",
    "Dhemaji",
    "Dhubri",
    "Dibrugarh",
    "Dima Hasao",
    "Goalpara",
    "Golaghat",
    "Hailakandi",
    "Hojai",
    "Jorhat",
    "Kamrup",
    "Kamrup Metro",
    "Karbi Anglong",
    "Karimganj",
    "Kokrajhar",
    "Lakhimpur",
    "Majuli"
  ],
  "BR": [
    "Araria",
    "Arwal",
    "Aurangabad",
    "Banka",
    "Begusarai",
    "Bhagalpur",
    "Bhojpur",
    "Buxar",
    "Darbhanga",
    "Gaya",
    "Gopalganj",
    "Jamui",
    "Jehanabad",
    "Kaimur (Bhabua)",
    "Katihar",
    "Khagaria",
    "Kishanganj",
    "Lakhisarai",
    "Madhepura",
    "Madhubani",
    "Munger",
    "Muzaffarpur",
    "Nalanda",
    "Nawada",
    "Pashchim Champaran"
  ],
  "CH": ["Chandigarh"],
  "CG": [
    "Balod",
    "Balodabazar-Bhatapara",
    "Balrampur Ramanujganj",
    "Bastar",
    "Bemetara",
    "Bijapur",
    "Bilaspur",
    "Dakshin Bastar Dantewada",
    "Dhamtari",
    "Durg",
    "Gariyaband",
    "Gaurela Pendra Marwahi",
    "Janjgir-Champa",
    "Jashpur",
    "Kabeerdham",
    "Sub Districts",
    "Kondagaon",
    "Korba",
    "Korea",
    "Mahasamund",
    "Sub Districts",
    "Mohla Manpur Ambagarh Chouki",
    "Mungeli",
    "Narayanpur",
    "Raigarh"
  ],
  "ND": ["Dadra And Nagar Haveli", "Daman", "Diu"],
  "DL": [
    "Central",
    "East",
    "New Delhi",
    "North",
    "North East",
    "North West",
    "Shahdara",
    "South",
    "South East",
    "South West",
    "West"
  ],
  "GA": ["North Goa", "South Goa"],
  "GJ": [
    "Ahmedabad",
    "Amreli",
    "Anand",
    "Arvalli",
    "Banas Kantha",
    "Bharuch",
    "Bhavnagar",
    "Botad",
    "Chhotaudepur",
    "Dahod",
    "Dangs",
    "Devbhumi Dwarka",
    "Gandhinagar",
    "Gir Somnath",
    "Jamnagar",
    "Junagadh",
    "Kachchh",
    "Kheda",
    "Mahesana",
    "Mahisagar",
    "Morbi",
    "Narmada",
    "Navsari",
    "Panch Mahals",
    "Patan"
  ],
  "HR": [
    "Ambala",
    "Bhiwani",
    "Charki Dadri",
    "Faridabad",
    "Fatehabad",
    "Gurugram",
    "Hisar",
    "Jhajjar",
    "Jind",
    "Kaithal",
    "Karnal",
    "Kurukshetra",
    "Mahendragarh",
    "Nuh",
    "Palwal",
    "Panchkula",
    "Panipat",
    "Rewari",
    "Rohtak",
    "Sirsa",
    "Sonipat",
    "Yamunanagar"
  ],
  "HP": [
    "Bilaspur",
    "Chamba",
    "Hamirpur",
    "Kangra",
    "Kinnaur",
    "Kullu",
    "Lahul And Spiti",
    "Mandi",
    "Shimla",
    "Sirmaur",
    "Solan",
    "Una"
  ],
  "JK": [
    "Anantnag",
    "Bandipora",
    "Baramulla",
    "Budgam",
    "Doda",
    "Ganderbal",
    "Jammu",
    "Kathua",
    "Kishtwar",
    "Kulgam",
    "Kupwara",
    "Poonch",
    "Pulwama",
    "Rajouri",
    "Ramban",
    "Reasi",
    "Samba",
    "Shopian",
    "Srinagar",
    "Udhampur"
  ],
  "JH": [
    "Bokaro",
    "Chatra",
    "Deoghar",
    "Dhanbad",
    "Dumka",
    "East Singhbum",
    "Garhwa",
    "Giridih",
    "Godda",
    "Gumla",
    "Hazaribagh",
    "Jamtara",
    "Khunti",
    "Koderma",
    "Latehar",
    "Lohardaga",
    "Pakur",
    "Palamu",
    "Ramgarh",
    "Ranchi",
    "Sahebganj",
    "Saraikela Kharsawan",
    "Simdega",
    "West Singhbhum"
  ],
  "KA": [
    "Bagalkote",
    "Ballari",
    "Belagavi",
    "Bengaluru Rural",
    "Bengaluru Urban",
    "Bidar",
    "Chamarajanagara",
    "Chikkaballapura",
    "Chikkamagaluru",
    "Chitradurga",
    "Dakshina Kannada",
    "Davangere",
    "Dharwad",
    "Gadag",
    "Hassan",
    "Haveri",
    "Kalaburagi",
    "Kodagu",
    "Kolar",
    "Koppal",
    "Mandya",
    "Mysuru",
    "Raichur",
    "Ramanagara",
    "Shivamogga"
  ],
  "KL": [
    "Alappuzha",
    "Ernakulam",
    "Idukki",
    "Kannur",
    "Kasaragod",
    "Kollam",
    "Kottayam",
    "Kozhikode",
    "Malappuram",
    "Palakkad",
    "Pathanamthitta",
    "Thiruvananthapuram",
    "Thrissur",
    "Wayanad"
  ],
  "LA": ["Kargil", "Leh Ladakh"],
  "LD": ["Lakshadweep District"],
  "MP": [
    "Agar-Malwa",
    "Alirajpur",
    "Anuppur",
    "Ashoknagar",
    "Balaghat",
    "Barwani",
    "Betul",
    "Bhind",
    "Bhopal",
    "Burhanpur",
    "Chhatarpur",
    "Chhindwara",
    "Damoh",
    "Datia",
    "Dewas",
    "Dhar",
    "Dindori",
    "Guna",
    "Gwalior",
    "Harda",
    "Indore",
    "Jabalpur",
    "Jhabua",
    "Katni",
    "Khandwa (East Nimar)"
  ],
  "MH": [
    "Ahmednagar",
    "Akola",
    "Amravati",
    "Beed",
    "Bhandara",
    "Buldhana",
    "Chandrapur",
    "Chhatrapati Sambhajinagar",
    "Dharashiv",
    "Dhule",
    "Gadchiroli",
    "Gondia",
    "Hingoli",
    "Jalgaon",
    "Jalna",
    "Kolhapur",
    "Latur",
    "Mumbai",
    "Mumbai Suburban",
    "Nagpur",
    "Nanded",
    "Nandurbar",
    "Nashik",
    "Palghar",
    "Parbhani"
  ],
  "MN": [
    "Bishnupur",
    "Chandel",
    "Churachandpur",
    "Imphal East",
    "Imphal West",
    "Sub Districts",
    "Kakching",
    "Kamjong",
    "Kangpokpi",
    "Sub Districts",
    "Pherzawl",
    "Senapati",
    "Tamenglong",
    "Tengnoupal",
    "Thoubal",
    "Ukhrul"
  ],
  "ML": [
    "East Garo Hills",
    "East Jaintia Hills",
    "East Khasi Hills",
    "Sub Districts",
    "North Garo Hills",
    "Ri Bhoi",
    "South Garo Hills",
    "South West Garo Hills",
    "South West Khasi Hills",
    "West Garo Hills",
    "West Jaintia Hills",
    "West Khasi Hills"
  ],
  "MZ": [
    "Aizawl",
    "Champhai",
    "Sub Districts",
    "Sub Districts",
    "Kolasib",
    "Lawngtlai",
    "Lunglei",
    "Mamit",
    "Sub Districts",
    "Serchhip",
    "Siaha"
  ],
  "NL": [
    "Chumoukedima",
    "Dimapur",
    "Kiphire",
    "Kohima",
    "Longleng",
    "Mokokchung",
    "Mon",
    "Sub Districts",
    "Noklak",
    "Peren",
    "Phek",
    "Shamator",
    "Tseminyu",
    "Tuensang",
    "Wokha",
    "Zunheboto"
  ],
  "OD": [
    "Anugul",
    "Balangir",
    "Baleshwar",
    "Bargarh",
    "Bhadrak",
    "Boudh",
    "Cuttack",
    "Deogarh",
    "Dhenkanal",
    "Gajapati",
    "Ganjam",
    "Jagatsinghapur",
    "Jajapur",
    "Jharsuguda",
    "Kalahandi",
    "Kandhamal",
    "Kendrapara",
    "Kendujhar",
    "Khordha",
    "Koraput",
    "Malkangiri",
    "Mayurbhanj",
    "Nabarangpur",
    "Nayagarh",
    "Nuapada"
  ],
  "PY": ["Karaikal", "Mahe", "Pondicherry", "Yanam"],
  "PB": [
    "Amritsar",
    "Barnala",
    "Bathinda",
    "Faridkot",
    "Fatehgarh Sahib",
    "Fazilka",
    "Ferozepur",
    "Gurdaspur",
    "Hoshiarpur",
    "Jalandhar",
    "Kapurthala",
    "Ludhiana",
    "Malerkotla",
    "Mansa",
    "Moga",
    "Pathankot",
    "Patiala",
    "Rupnagar",
    "S.A.S Nagar",
    "Sangrur",
    "Shahid Bhagat Singh Nagar",
    "Sri Muktsar Sahib",
    "Tarn Taran"
  ],
  "RJ": [
    "Ajmer",
    "Alwar",
    "Anoopgarh",
    "Balotra",
    "Banswara",
    "Baran",
    "Barmer",
    "Beawar",
    "Bharatpur",
    "Bhilwara",
    "Bikaner",
    "Bundi",
    "Chittorgarh",
    "Churu",
    "Dausa",
    "Deeg",
    "Dholpur",
    "Sub Districts",
    "Dudu",
    "Dungarpur",
    "Ganganagar",
    "Gangapurcity",
    "Hanumangarh",
    "Jaipur",
    "Sub Districts"
  ],
  "SK": [
    "Sub Districts",
    "Sub Districts",
    "Mangan",
    "Sub Districts",
    "Sub Districts",
    "Soreng"
  ],
  "TN": [
    "Ariyalur",
    "Chengalpattu",
    "Chennai",
    "Coimbatore",
    "Cuddalore",
    "Dharmapuri",
    "Dindigul",
    "Erode",
    "Kallakurichi",
    "Kancheepuram",
    "Kanniyakumari",
    "Karur",
    "Krishnagiri",
    "Madurai",
    "Mayiladuthurai",
    "Nagapattinam",
    "Namakkal",
    "Perambalur",
    "Pudukkottai",
    "Ramanathapuram",
    "Sub Districts",
    "Salem",
    "Sivaganga",
    "Tenkasi",
    "Thanjavur"
  ],
  "TS": [
    "Adilabad",
    "Bhadradri Kothagudem",
    "Hanumakonda",
    "Hyderabad",
    "Jagitial",
    "Jangoan",
    "Jayashankar Bhupalapally",
    "Jogulamba Gadwal",
    "Kamareddy",
    "Karimnagar",
    "Khammam",
    "Kumuram Bheem Asifabad",
    "Mahabubabad",
    "Mahabubnagar",
    "Mancherial",
    "Medak",
    "Medchal Malkajgiri",
    "Mulugu",
    "Nagarkurnool",
    "Nalgonda",
    "Narayanpet",
    "Nirmal",
    "Nizamabad",
    "Peddapalli",
    "Rajanna Sircilla"
  ],
  "TR": [
    "Dhalai",
    "Gomati",
    "Khowai",
    "North Tripura",
    "Sepahijala",
    "South Tripura",
    "Unakoti",
    "West Tripura"
  ],
  "UP": [
    "Agra",
    "Aligarh",
    "Ambedkar Nagar",
    "Amethi",
    "Amroha",
    "Auraiya",
    "Ayodhya",
    "Azamgarh",
    "Baghpat",
    "Bahraich",
    "Ballia",
    "Balrampur",
    "Banda",
    "Bara Banki",
    "Bareilly",
    "Basti",
    "Bhadohi",
    "Bijnor",
    "Budaun",
    "Bulandshahr",
    "Chandauli",
    "Chitrakoot",
    "Deoria",
    "Etah",
    "Etawah"
  ],
  "UK": [
    "Almora",
    "Bageshwar",
    "Chamoli",
    "Champawat",
    "Dehradun",
    "Haridwar",
    "Nainital",
    "Pauri Garhwal",
    "Pithoragarh",
    "Rudra Prayag",
    "Tehri Garhwal",
    "Udam Singh Nagar",
    "Uttar Kashi"
  ],
  "WB": [
    "Alipurduar",
    "Bankura",
    "Birbhum",
    "Cooch Behar",
    "Dakshin Dinajpur",
    "Darjeeling",
    "Hooghly",
    "Howrah",
    "Jalpaiguri",
    "Jhargram",
    "Kalimpong",
    "Sub Districts",
    "Malda",
    "Murshidabad",
    "Nadia",
    "North 24 Parganas",
    "Paschim Bardhaman",
    "Paschim Medinipur",
    "Purba Bardhaman",
    "Purba Medinipur",
    "Purulia",
    "South 24 Parganas",
    "Uttar Dinajpur"
  ]
}
```