# Basic Stock Information API

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
        "previousClose": 157.9,
        "open": 156.1,
        "dayLow": 155.0,
        "dayHigh": 157.9,
        "volume": 26453000,
        "averageVolume": 29029810,
        ...
    }
}
