# Image Triangle Detection

## Dashboard Is now on [Heroku](https://smartrackapi.herokuapp.com/)

## List Of Racks Setup And Their Configurations

### 1. Overland Park
Configuration Information

| Attribute | Value | Instructions |
| --------- | -------- | ---------- |
| Rack No   | 000003 | |
| Name      | T1757 Overland Park | |
| Address   | 12200 Blue Valley PKVY, Overland Park, KS | |
| Shelves   | 4 | |
| Shelf Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/shelves/000003) | |
| Traffic Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/traffic/000003) | |
| Send Yesterday Report | [Send Report](https://smartrackapi.herokuapp.com/shelves/api/sendreport/yesterday/000003) | |
| Show Report Or Any day Report | [Show Report](https://smartrackapi.herokuapp.com/shelves/api/showreport/yesterday/000003) | This Will Show report but will not send |
> Note:
To Send Report of any day use the below link
 https://smartrackapi.herokuapp.com/shelves/api/sendreport/${days_before_yesterday}/${racknum}
  days before yesterday could be -> 0 -> Yesterday, 1 -> Day Before Yesterday, 2 -> 2 Days Before Yesterday And So On
Also known as Target 1

### 2. Olathe
Configuration Information

| Attribute | Value |
| --------- | -------- |
| Rack No   | 000004 |
| Name      | T1756 Olathe |
| Address   | 15345 W 119TH ST, Olathe, KS |
| Shelves   | 4 |
| Shelf Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/shelves/000004) |
| Traffic Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/traffic/000004) |
> Note:
Also known as Target 2

### 3. Target A
Configuration Information

| Attribute | Value |
| --------- | -------- |
| Rack No   | 000005 |
| Name      | T1775 TARGET-DL-1 |
| Address   | 16731 Coit Rd, Dalls, TX 75248 |
| Shelves   | 4 |
| Hotspot   | KProject |
| Device    |   ATNT   |
| Shelf Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/shelves/000005) |
| Traffic Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/traffic/000005) |

### 4. Target B
Configuration Information

| Attribute | Value |
| --------- | -------- |
| Rack No   | 000006 |
| Name      | TARGET-DL-2 |
| Address   | 16731 Coit Rd, Dalls, TX 75248 |
| Shelves   | 4 |
| Hotspot   | KProject |
| Device    |   ATNT   |
| Shelf Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/shelves/000006) |
| Traffic Dashboard | [Dashboard](https://smartrackapi.herokuapp.com/traffic/000006) |
