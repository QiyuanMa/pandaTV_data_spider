# panda_data_spider
The project collected 1712396 interaction datas from live-sharing platform PandasTV based on python scrapy.
No worry about the quota limits because no api is applied. 

File panda includes all python programs. Run python and all data would collected and stored into mongodb database.
File panda_data includes all data exported in json.

In panda_data:
panda_id.json includes 23436 hosts information, a case of them is:
    { 
        "_id" : ObjectId("5bde46a10fd265e2a6b104e1"), 
        "tid" : "2018-11-19 21:35:51", 
        "classification" : {
            "cname" : "游戏宝贝", 
            "ename" : "gbaby"
        }, 
        "id" : "194737", 
        "rid" : NumberInt(23279744), 
        "nickname" : "狐筱念", 
        "person_num" : NumberInt(4364), 
        "ticket_rank_info" : {
            "rank" : NumberInt(460), 
            "score" : NumberInt(14)
        }, 
        "host_level_info" : {
            "val" : 1282.00142, 
            "c_lv" : NumberInt(7), 
            "c_lv_val" : NumberInt(1117), 
            "n_lv" : NumberInt(8), 
            "n_lv_val" : NumberInt(1390), 
            "plays_day" : NumberInt(309), 
            "bamboo_user" : 17.437102, 
            "gift_user" : 497.595128, 
            "gift_cnt" : 457.96919, 
            "vip" : NumberInt(0)
        }, 
        "room_key" : "1ddf47b635c76577bc1acc7237d5d195"
    }
panda_room.json includes all the video rooms information based on the 23436 host id information, which includes fans, popularity, host revuenue, received gifts, host ranking,etc.
A case is like:
{ 
    "_id" : ObjectId("5bde46a10fd265e2a6b104e2"), 
    "id" : "194737", 
    "fans" : NumberInt(2584), 
    "total_rank" : [
        {
            "rid" : NumberInt(5543040), 
            "nickname" : "随缘zy", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(112858386), 
            "nickname" : "路大叔_", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(78768300), 
            "nickname" : "超大冷森5", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(34932560), 
            "nickname" : "私念的麦克风", 
            "score" : NumberInt(3313643)
        }, 
        {
            "rid" : NumberInt(6156812), 
            "nickname" : "不爱你的加菲喵", 
            "score" : NumberInt(3241860)
        }, 
        {
            "rid" : NumberInt(51614066), 
            "nickname" : "兄弟你别叫好吧", 
            "score" : NumberInt(2955640)
        }, 
        {
            "rid" : NumberInt(68929664), 
            "nickname" : "阿di丶无双", 
            "score" : NumberInt(2880118)
        }, 
        {
            "rid" : NumberInt(145728340), 
            "nickname" : "熊猫194737狐媚娘", 
            "score" : NumberInt(2834910)
        }, 
        {
            "rid" : NumberInt(4835572), 
            "nickname" : "狮子暗", 
            "score" : NumberInt(2468701)
        }, 
        {
            "rid" : NumberInt(98923962), 
            "nickname" : "月小兔兔兔兔兔兔", 
            "score" : NumberInt(2076300)
        }
    ], 
    "weekly_rank" : [
        {
            "rid" : NumberInt(4835572), 
            "nickname" : "狮子暗", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(42828630), 
            "nickname" : "狐筱念的XMING", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(145728340), 
            "nickname" : "熊猫194737狐媚娘", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(78768300), 
            "nickname" : "超大冷森5", 
            "score" : NumberInt(476240)
        }, 
        {
            "rid" : NumberInt(31708058), 
            "nickname" : "超级玛丽不麻利", 
            "score" : NumberInt(377500)
        }, 
        {
            "rid" : NumberInt(30266034), 
            "nickname" : "狐筱念的VEIN", 
            "score" : NumberInt(372580)
        }, 
        {
            "rid" : NumberInt(140640896), 
            "nickname" : "狐筱念的小黄书", 
            "score" : NumberInt(369920)
        }, 
        {
            "rid" : NumberInt(5543040), 
            "nickname" : "随缘zy", 
            "score" : NumberInt(283600)
        }, 
        {
            "rid" : NumberInt(62129446), 
            "nickname" : "清风烈酒何你", 
            "score" : NumberInt(272732)
        }, 
        {
            "rid" : NumberInt(101002694), 
            "nickname" : "羽盛盛盛盛盛盛", 
            "score" : NumberInt(228800)
        }
    ], 
    "popularity" : NumberInt(825580)
}
{ 
    "_id" : ObjectId("5bde46a20fd265e2a6b104fa"), 
    "id" : "990599", 
    "total_rank" : [
        {
            "rid" : NumberInt(34610448), 
            "nickname" : "舵落口", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(29076024), 
            "nickname" : "靜女如姝", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(38092412), 
            "nickname" : "老顽童oldboy", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(66924844), 
            "nickname" : "杨柳腰", 
            "score" : NumberInt(25300)
        }, 
        {
            "rid" : NumberInt(21669890), 
            "nickname" : "QQv爱屋及乌", 
            "score" : NumberInt(25100)
        }, 
        {
            "rid" : NumberInt(150629936), 
            "nickname" : "娜娜的小哪吒", 
            "score" : NumberInt(24600)
        }, 
        {
            "rid" : NumberInt(60953086), 
            "nickname" : "九鱼猫易人", 
            "score" : NumberInt(23900)
        }, 
        {
            "rid" : NumberInt(127525276), 
            "nickname" : "微笑大魔王a", 
            "score" : NumberInt(21000)
        }, 
        {
            "rid" : NumberInt(69154204), 
            "nickname" : "宾克斯的醉酒丶", 
            "score" : NumberInt(20300)
        }, 
        {
            "rid" : NumberInt(149840076), 
            "nickname" : "智能哔哩", 
            "score" : NumberInt(16400)
        }
    ], 
    "weekly_rank" : [
        {
            "rid" : NumberInt(36506152), 
            "nickname" : "王爷少爷", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(31106080), 
            "nickname" : "不甜家的皮皮怪", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(76771360), 
            "nickname" : "ST逆行风", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(107872088), 
            "nickname" : "绝世好二爷", 
            "score" : NumberInt(1000)
        }, 
        {
            "rid" : NumberInt(106764860), 
            "nickname" : "朝鲜牛肉干", 
            "score" : NumberInt(300)
        }, 
        {
            "rid" : NumberInt(110354896), 
            "nickname" : "明天更好9992", 
            "score" : NumberInt(200)
        }, 
        {
            "rid" : NumberInt(107024726), 
            "nickname" : "深深深几何", 
            "score" : NumberInt(200)
        }, 
        {
            "rid" : NumberInt(23873856), 
            "nickname" : "逆时针的菜", 
            "score" : NumberInt(100)
        }
    ], 
    "fans" : NumberInt(995), 
    "popularity" : NumberInt(554)
}
{ 
    "_id" : ObjectId("5bde46a20fd265e2a6b10500"), 
    "id" : "1867124", 
    "total_rank" : [
        {
            "rid" : NumberInt(100689052), 
            "nickname" : "你当如何回忆我", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(4478984), 
            "nickname" : "牌主任", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(88897916), 
            "nickname" : "简简单单的等待丶", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(43952200), 
            "nickname" : "飞翔鱼", 
            "score" : NumberInt(958820)
        }, 
        {
            "rid" : NumberInt(91377178), 
            "nickname" : "温酒沏茶_怪大叔", 
            "score" : NumberInt(830460)
        }, 
        {
            "rid" : NumberInt(83156064), 
            "nickname" : "星空下的小狮子", 
            "score" : NumberInt(826900)
        }, 
        {
            "rid" : NumberInt(83474562), 
            "nickname" : "Dream_Zhao", 
            "score" : NumberInt(799953)
        }, 
        {
            "rid" : NumberInt(115390886), 
            "nickname" : "路过的小呱唧", 
            "score" : NumberInt(772252)
        }, 
        {
            "rid" : NumberInt(40232620), 
            "nickname" : "空白de你", 
            "score" : NumberInt(673380)
        }, 
        {
            "rid" : NumberInt(88354252), 
            "nickname" : "简单直接的坏蛋", 
            "score" : NumberInt(640920)
        }
    ], 
    "fans" : NumberInt(6321), 
    "weekly_rank" : [
        {
            "rid" : NumberInt(154731532), 
            "nickname" : "那个谁在哪呢", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(83156064), 
            "nickname" : "星空下的小狮子", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(43952200), 
            "nickname" : "飞翔鱼", 
            "score" : NumberInt(0)
        }, 
        {
            "rid" : NumberInt(66120362), 
            "nickname" : "不喜伤感", 
            "score" : NumberInt(50500)
        }, 
        {
            "rid" : NumberInt(91377178), 
            "nickname" : "温酒沏茶_怪大叔", 
            "score" : NumberInt(37200)
        }, 
        {
            "rid" : NumberInt(62482436), 
            "nickname" : "蚀风q", 
            "score" : NumberInt(12700)
        }, 
        {
            "rid" : NumberInt(135273902), 
            "nickname" : "章正愚2", 
            "score" : NumberInt(12000)
        }, 
        {
            "rid" : NumberInt(68929664), 
            "nickname" : "阿di丶无双", 
            "score" : NumberInt(10000)
        }, 
        {
            "rid" : NumberInt(5353568), 
            "nickname" : "古乍子", 
            "score" : NumberInt(6000)
        }, 
        {
            "rid" : NumberInt(112479138), 
            "nickname" : "房管来桶泡面", 
            "score" : NumberInt(5700)
        }
    ], 
    "popularity" : NumberInt(87300)
}
