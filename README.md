# panda_data_spider
The project collected 1712396 interaction datas(hosts popularity, received gifts, ranking.etc) from live-sharing platform PandasTV based on python scrapy.
No worry about the quota limits because no api is applied. 

File panda includes all python programs. Run python and all data would collected and stored into mongodb database.
File panda_data includes all data exported in json.

In panda_data:
panda_id.json includes 23436 hosts information, includes room id, publish time, classification, host id, host nickname, viewers, tickets rank, tickets score, host level information(value, exp, play days, received bomboos, received gifts amount, received gifts value, vip).etc.

panda_room.json includes all the video rooms information based on the 23436 host id information, 
which includes id, fans, total ranking(room id, nickname, score), weekly ranking, popularity etc.


