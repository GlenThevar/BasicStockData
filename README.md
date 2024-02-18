# COMPLETE INFO OF INDIAN COMPANIES BASED ON THEIR SYMBOL 

This API allows users to retrieve information about a stock using its ticker symbol.

## Base URL

The base URL for this API is `https://stocks2.onrender.com/apidocs/`

## Endpoints

### Retrieve Stock Information

- **URL:** `/stock-information`
- **Method:** `GET`
- **Description:** Retrieves information about a specified stock using its ticker symbol.
- **Query Parameters:**
  - `ticker` (required): The stock symbol (ticker) for which information is requested.
- **Responses:**
  - `200 OK`: Successful response containing information about the specified stock.
  - `400 Bad Request`: Indicates that the provided stock symbol is invalid or not found.
  - `500 Internal Server Error`: Indicates an issue with retrieving stock information.

### Example

**Response:**
```json
{
  "information": {
    "52WeekChange": 0.068573594,
    "SandP52WeekChange": 0.25222528,
    "address1": "Plot No. 44/97 A",
    "address2": "3rd cross Electronic City Hosur Road",
    "auditRisk": 6,
    "averageDailyVolume10Day": 4619790,
    "averageVolume": 6395338,
    "averageVolume10days": 4619790,
    "beta": 0.565,
    "boardRisk": 2,
    "bookValue": 2.323,
    "city": "Bengaluru",
    "companyOfficers": [
      {
        "age": 67,
        "exercisedValue": 0,
        "maxAge": 1,
        "name": "Mr. Nandan M. Nilekani",
        "title": "Co-Founder & Chairman",
        "unexercisedValue": 0,
        "yearBorn": 1956
      },
      {
        "age": 59,
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Salil Satish Parekh",
        "title": "MD, CEO & Director",
        "totalPay": 264736615,
        "unexercisedValue": 0,
        "yearBorn": 1964
      },
      {
        "age": 57,
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Nilanjan  Roy ACA, B.Com",
        "title": "Chief Financial Officer",
        "totalPay": 50974682,
        "unexercisedValue": 0,
        "yearBorn": 1966
      },
      {
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Anand  Swaminathan",
        "title": "Executive VP and Segment Head of Communication, Media & Technology",
        "unexercisedValue": 0
      },
      {
        "age": 58,
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Ms. Inderpreet  Sawhney",
        "title": "Executive VP, Group General Counsel & Chief Compliance Officer",
        "totalPay": 95445920,
        "unexercisedValue": 0,
        "yearBorn": 1965
      },
      {
        "age": 52,
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Shaji  Mathew",
        "title": "Group Head of HR, Exec VP & Svc Offering Head of Fin Svcs, Healthcare, Ins and Life Sciences",
        "totalPay": 10528928,
        "unexercisedValue": 0,
        "yearBorn": 1971
      },
      {
        "age": 51,
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Karmesh Gul Vaswani",
        "title": "Executive VP & Segment Head of CPG, Logistics & Retail",
        "unexercisedValue": 0,
        "yearBorn": 1972
      },
      {
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Jasmeet  Singh",
        "title": "Executive VP & Segment Head of Manufacturing",
        "unexercisedValue": 0
      },
      {
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Ms. Martha G. King",
        "title": "Executive VP & Chief Client Officer",
        "unexercisedValue": 0
      },
      {
        "age": 60,
        "exercisedValue": 0,
        "fiscalYear": 2023,
        "maxAge": 1,
        "name": "Mr. Frank Lord Satterthwaite",
        "title": "Senior Vice President of Delivery, FSHIL",
        "unexercisedValue": 0,
        "yearBorn": 1963
      }
    ],
    "compensationAsOfEpochDate": 1703980800,
    "compensationRisk": 5,
    "country": "India",
    "currency": "INR",
    "currentPrice": 1701.65,
    "currentRatio": 1.986,
    "dayHigh": 1709,
    "dayLow": 1687.95,
    "debtToEquity": 10.871,
    "dividendRate": 36,
    "dividendYield": 0.0212,
    "earningsGrowth": -0.068,
    "earningsQuarterlyGrowth": -0.084,
    "ebitda": 4249999872,
    "ebitdaMargins": 0.22909,
    "enterpriseToEbitda": 1656.934,
    "enterpriseToRevenue": 379.58,
    "enterpriseValue": 7041970601984,
    "exDividendDate": 1698192000,
    "exchange": "NSI",
    "fax": "91 80 2852 0362",
    "fiftyDayAverage": 1601.429,
    "fiftyTwoWeekHigh": 1733,
    "fiftyTwoWeekLow": 1185.3,
    "financialCurrency": "USD",
    "firstTradeDateEpochUtc": 820467900,
    "fiveYearAvgDividendYield": 2.12,
    "floatShares": 3576639677,
    "forwardEps": 66.94,
    "forwardPE": 25.420525,
    "freeCashflow": 1911750016,
    "fullTimeEmployees": 322663,
    "gmtOffSetMilliseconds": 19800000,
    "governanceEpochDate": 1706745600,
    "grossMargins": 0.29700002,
    "heldPercentInsiders": 0.15985,
    "heldPercentInstitutions": 0.46849,
    "impliedSharesOutstanding": 4139290112,
    "industry": "Information Technology Services",
    "industryDisp": "Information Technology Services",
    "industryKey": "information-technology-services",
    "lastDividendDate": 1698192000,
    "lastDividendValue": 18,
    "lastFiscalYearEnd": 1680220800,
    "lastSplitDate": 1536019200,
    "lastSplitFactor": "2:1",
    "longBusinessSummary": "Infosys Limited, together with its subsidiaries, provides consulting, technology, outsourcing, and next-generation digital services in North America, Europe, India, and internationally. It provides application management and application development services, independent validation solutions, product engineering and management, infrastructure management services, traditional enterprise application implementation, support, and integration services. The company's products and platforms include Finacle, a core banking solution; Edge suite of products; Panaya platform, Infosys Equinox, Infosys Helix, Infosys Applied AI, Infosys Cortex, and Stater digital platforms; and Infosys McCamish, an insurance platform. It serves enterprises in the financial services and insurance, manufacturing, retail, consumer packaged goods, logistics, energy, utilities, resources, services, communications, telecom OEM, media, hi-tech, and life sciences and healthcare industries. The company has a collaboration with Microsoft to accelerate and democratize industry-wide adoption of generative AI; and strategic collaboration with Amazon Web Services Inc to deliver technology transformation and industry specific solutions to financial organizations. The company was formerly known as Infosys Technologies Limited and changed its name to Infosys Limited in June 2011. Infosys Limited was incorporated in 1981 and is headquartered in Bengaluru, India.",
    "longName": "Infosys Limited",
    "marketCap": 7043623157760,
    "maxAge": 86400,
    "messageBoardId": "finmb_398006",
    "mostRecentQuarter": 1703980800,
    "netIncomeToCommon": 2952000000,
    "nextFiscalYearEnd": 1711843200,
    "numberOfAnalystOpinions": 41,
    "open": 1689,
    "operatingCashflow": 3041999872,
    "operatingMargins": 0.20502001,
    "overallRisk": 2,
    "payoutRatio": 0.6025,
    "pegRatio": 3.19,
    "phone": "91 80 2852 0261",
    "previousClose": 1676.35,
    "priceHint": 2,
    "priceToBook": 732.52264,
    "priceToSalesTrailing12Months": 379.6692,
    "profitMargins": 0.15912,
    "quickRatio": 1.696,
    "quoteType": "EQUITY",
    "recommendationKey": "buy",
    "recommendationMean": 2.3,
    "regularMarketDayHigh": 1709,
    "regularMarketDayLow": 1687.95,
    "regularMarketOpen": 1689,
    "regularMarketPreviousClose": 1676.35,
    "regularMarketVolume": 4880071,
    "returnOnAssets": 0.1571,
    "returnOnEquity": 0.31604,
    "revenueGrowth": 0.001,
    "revenuePerShare": 4.481,
    "sector": "Technology",
    "sectorDisp": "Technology",
    "sectorKey": "technology",
    "shareHolderRightsRisk": 1,
    "sharesOutstanding": 4139290112,
    "shortName": "INFOSYS LTD",
    "symbol": "INFY.NS",
    "targetHighPrice": 2000,
    "targetLowPrice": 1160,
    "targetMeanPrice": 1636.28,
    "targetMedianPrice": 1690,
    "timeZoneFullName": "Asia/Kolkata",
    "timeZoneShortName": "IST",
    "totalCash": 2598000128,
    "totalCashPerShare": 0.628,
    "totalDebt": 1051000000,
    "totalRevenue": 18552000512,
    "trailingAnnualDividendRate": 0.43,
    "trailingAnnualDividendYield": 0.0002565097,
    "trailingEps": 58.88,
    "trailingPE": 28.900305,
    "trailingPegRatio": 2.494,
    "twoHundredDayAverage": 1442.9034,
    "underlyingSymbol": "INFY.NS",
    "uuid": "6e0e3969-0bf9-3676-8a5c-d91501277ca6",
    "volume": 4880071,
    "website": "https://www.infosys.com",
    "zip": "560100"
  }
}

