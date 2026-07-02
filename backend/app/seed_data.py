"""
种子数据模块

包含所有菜谱、分类的初始数据。
用于初始化数据库，提供丰富的菜谱内容。
"""

from datetime import datetime
from .database import recipes_collection, categories_collection


# ==================== 分类数据 ====================

CATEGORIES = [
    {"name": "荤菜", "icon": "🍖", "order": 1},
    {"name": "素菜", "icon": "🥬", "order": 2},
    {"name": "汤羹", "icon": "🍲", "order": 3},
    {"name": "主食", "icon": "🍚", "order": 4},
    {"name": "凉菜", "icon": "🥗", "order": 5},
    {"name": "甜点", "icon": "🍰", "order": 6},
    {"name": "饮品", "icon": "🥤", "order": 7},
]


# ==================== 菜谱数据 ====================

RECIPES = [
    # ==================== 荤菜 ====================
    {
        "name": "红烧肉",
        "category": "荤菜",
        "subcategory": "猪肉",
        "image": "https://images.unsplash.com/photo-1623689048105-a17b1e1936b8?w=400",
        "description": "经典家常菜，肥而不腻，入口即化",
        "ingredients": ["五花肉500g", "生抽2勺", "老抽1勺", "冰糖适量", "八角2个", "桂皮1小块", "料酒1勺", "姜片3片"],
        "steps": [
            {"order": 1, "desc": "五花肉切块，冷水下锅焯水去腥"},
            {"order": 2, "desc": "锅中放油，小火炒化冰糖至焦糖色"},
            {"order": 3, "desc": "放入五花肉翻炒上色"},
            {"order": 4, "desc": "加入料酒、生抽、老抽、八角、桂皮、姜片"},
            {"order": 5, "desc": "加入没过肉的热水，大火烧开后转小火炖40分钟"},
            {"order": 6, "desc": "大火收汁即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "60分钟",
        "tags": ["下饭", "经典", "宴客"]
    },
    {
        "name": "糖醋排骨",
        "category": "荤菜",
        "subcategory": "猪肉",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
        "description": "酸甜可口，外酥里嫩",
        "ingredients": ["排骨500g", "生抽2勺", "醋3勺", "白糖3勺", "料酒1勺", "番茄酱2勺"],
        "steps": [
            {"order": 1, "desc": "排骨切小段，冷水下锅焯水"},
            {"order": 2, "desc": "捞出沥干，用厨房纸吸干水分"},
            {"order": 3, "desc": "锅中放油，炸排骨至金黄"},
            {"order": 4, "desc": "调糖醋汁：生抽、醋、糖、番茄酱混合"},
            {"order": 5, "desc": "锅留底油，倒入糖醋汁煮至冒泡"},
            {"order": 6, "desc": "放入排骨翻炒均匀即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "40分钟",
        "tags": ["酸甜", "下饭", "儿童喜欢"]
    },
    {
        "name": "宫保鸡丁",
        "category": "荤菜",
        "subcategory": "鸡肉",
        "image": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=400",
        "description": "川菜经典，麻辣鲜香",
        "ingredients": ["鸡胸肉300g", "花生米50g", "干辣椒10个", "花椒1勺", "葱姜蒜适量"],
        "steps": [
            {"order": 1, "desc": "鸡胸肉切丁，加料酒、淀粉腌制10分钟"},
            {"order": 2, "desc": "花生米炒熟备用"},
            {"order": 3, "desc": "锅中放油，爆香干辣椒和花椒"},
            {"order": 4, "desc": "放入鸡丁翻炒至变色"},
            {"order": 5, "desc": "加入调好的宫保汁翻炒"},
            {"order": 6, "desc": "最后加入花生米翻炒均匀"}
        ],
        "price_hearts": 4,
        "difficulty": "中等",
        "cook_time": "25分钟",
        "tags": ["川菜", "麻辣", "下饭"]
    },
    {
        "name": "番茄炒蛋",
        "category": "荤菜",
        "subcategory": "鸡蛋",
        "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400",
        "description": "家常菜之王，简单美味",
        "ingredients": ["番茄2个", "鸡蛋3个", "葱花适量", "盐适量", "糖少许"],
        "steps": [
            {"order": 1, "desc": "番茄切块，鸡蛋打散加盐"},
            {"order": 2, "desc": "锅中放油，炒鸡蛋至凝固盛出"},
            {"order": 3, "desc": "锅中放油，炒番茄至出汁"},
            {"order": 4, "desc": "加入炒好的鸡蛋翻炒"},
            {"order": 5, "desc": "加盐、少许糖调味，撒葱花出锅"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["家常", "快手", "下饭"]
    },
    {
        "name": "可乐鸡翅",
        "category": "荤菜",
        "subcategory": "鸡肉",
        "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=400",
        "description": "甜香四溢，老少皆宜",
        "ingredients": ["鸡翅8个", "可乐1罐", "生抽2勺", "老抽1勺", "姜片3片"],
        "steps": [
            {"order": 1, "desc": "鸡翅划两刀，冷水下锅焯水"},
            {"order": 2, "desc": "锅中放油，煎鸡翅至两面金黄"},
            {"order": 3, "desc": "加入生抽、老抽、姜片"},
            {"order": 4, "desc": "倒入可乐没过鸡翅"},
            {"order": 5, "desc": "大火烧开转小火炖15分钟"},
            {"order": 6, "desc": "大火收汁即可"}
        ],
        "price_hearts": 4,
        "difficulty": "简单",
        "cook_time": "30分钟",
        "tags": ["甜味", "儿童喜欢", "简单"]
    },
    {
        "name": "麻婆豆腐",
        "category": "荤菜",
        "subcategory": "豆制品",
        "image": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=400",
        "description": "麻辣鲜香，下饭神器",
        "ingredients": ["豆腐1块", "猪肉末100g", "豆瓣酱1勺", "花椒粉适量", "葱花适量"],
        "steps": [
            {"order": 1, "desc": "豆腐切块，焯水去豆腥"},
            {"order": 2, "desc": "锅中放油，炒肉末至变色"},
            {"order": 3, "desc": "加入豆瓣酱炒出红油"},
            {"order": 4, "desc": "加入适量水烧开"},
            {"order": 5, "desc": "放入豆腐轻轻推动，炖5分钟"},
            {"order": 6, "desc": "撒花椒粉、葱花出锅"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "20分钟",
        "tags": ["川菜", "麻辣", "下饭"]
    },
    {
        "name": "红烧鱼",
        "category": "荤菜",
        "subcategory": "鱼虾",
        "image": "https://images.unsplash.com/photo-1534766555764-ce878a4e947d?w=400",
        "description": "鲜嫩入味，年年有余",
        "ingredients": ["鲫鱼1条", "生抽2勺", "老抽1勺", "醋1勺", "葱姜蒜适量"],
        "steps": [
            {"order": 1, "desc": "鱼处理干净，两面划刀"},
            {"order": 2, "desc": "锅中放油，煎鱼至两面金黄"},
            {"order": 3, "desc": "加入葱姜蒜爆香"},
            {"order": 4, "desc": "加入生抽、老抽、醋和适量水"},
            {"order": 5, "desc": "大火烧开转小火炖15分钟"},
            {"order": 6, "desc": "大火收汁，撒葱花出锅"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "30分钟",
        "tags": ["鲜美", "宴客", "寓意好"]
    },
    {
        "name": "回锅肉",
        "category": "荤菜",
        "subcategory": "猪肉",
        "image": "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=400",
        "description": "川菜之首，肥而不腻",
        "ingredients": ["五花肉300g", "青蒜100g", "豆瓣酱1勺", "甜面酱1勺"],
        "steps": [
            {"order": 1, "desc": "五花肉整块煮至八成熟"},
            {"order": 2, "desc": "捞出放凉后切薄片"},
            {"order": 3, "desc": "青蒜切段"},
            {"order": 4, "desc": "锅中不放油，煸炒肉片至出油卷曲"},
            {"order": 5, "desc": "加入豆瓣酱、甜面酱炒香"},
            {"order": 6, "desc": "加入青蒜翻炒均匀即可"}
        ],
        "price_hearts": 4,
        "difficulty": "中等",
        "cook_time": "25分钟",
        "tags": ["川菜", "经典", "下饭"]
    },
    {
        "name": "清蒸鲈鱼",
        "category": "荤菜",
        "subcategory": "鱼虾",
        "image": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=400",
        "description": "鲜嫩清甜，原汁原味",
        "ingredients": ["鲈鱼1条", "葱丝适量", "姜丝适量", "蒸鱼豉油2勺", "热油适量"],
        "steps": [
            {"order": 1, "desc": "鲈鱼处理干净，两面划刀"},
            {"order": 2, "desc": "鱼身放姜丝，肚子里放葱姜"},
            {"order": 3, "desc": "水烧开后大火蒸8-10分钟"},
            {"order": 4, "desc": "倒掉蒸出的水，去掉旧葱姜"},
            {"order": 5, "desc": "放上新的葱丝姜丝"},
            {"order": 6, "desc": "淋上蒸鱼豉油，浇热油即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "20分钟",
        "tags": ["清淡", "鲜美", "宴客"]
    },
    {
        "name": "水煮牛肉",
        "category": "荤菜",
        "subcategory": "牛肉",
        "image": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?w=400",
        "description": "麻辣鲜香，肉质嫩滑",
        "ingredients": ["牛肉300g", "豆芽200g", "豆瓣酱2勺", "花椒1勺", "干辣椒10个"],
        "steps": [
            {"order": 1, "desc": "牛肉切片，加蛋清、淀粉腌制"},
            {"order": 2, "desc": "豆芽焯水铺在碗底"},
            {"order": 3, "desc": "锅中放油，炒豆瓣酱出红油"},
            {"order": 4, "desc": "加入水烧开，放入牛肉片"},
            {"order": 5, "desc": "牛肉变色后连汤倒入碗中"},
            {"order": 6, "desc": "撒上花椒、干辣椒，浇热油"}
        ],
        "price_hearts": 5,
        "difficulty": "困难",
        "cook_time": "30分钟",
        "tags": ["川菜", "麻辣", "宴客"]
    },
    {
        "name": "啤酒鸭",
        "category": "荤菜",
        "subcategory": "鸭肉",
        "image": "https://images.unsplash.com/photo-1518492104633-130d0cc84637?w=400",
        "description": "酒香浓郁，鸭肉酥烂",
        "ingredients": ["鸭肉500g", "啤酒1罐", "青椒2个", "生抽2勺", "老抽1勺"],
        "steps": [
            {"order": 1, "desc": "鸭肉切块，冷水下锅焯水"},
            {"order": 2, "desc": "锅中放油，炒鸭肉至出油"},
            {"order": 3, "desc": "加入生抽、老抽翻炒上色"},
            {"order": 4, "desc": "倒入啤酒没过鸭肉"},
            {"order": 5, "desc": "大火烧开转小火炖30分钟"},
            {"order": 6, "desc": "加入青椒翻炒，大火收汁"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "50分钟",
        "tags": ["酒香", "下饭", "宴客"]
    },
    {
        "name": "孜然羊肉",
        "category": "荤菜",
        "subcategory": "羊肉",
        "image": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=400",
        "description": "香气扑鼻，肉质鲜嫩",
        "ingredients": ["羊肉300g", "孜然粉2勺", "辣椒粉1勺", "洋葱半个", "香菜适量"],
        "steps": [
            {"order": 1, "desc": "羊肉切片，加料酒、淀粉腌制"},
            {"order": 2, "desc": "洋葱切丝"},
            {"order": 3, "desc": "锅中放油，大火爆炒羊肉至变色"},
            {"order": 4, "desc": "加入洋葱翻炒"},
            {"order": 5, "desc": "撒入孜然粉、辣椒粉翻炒"},
            {"order": 6, "desc": "出锅前撒香菜即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "20分钟",
        "tags": ["西北菜", "烧烤味", "下酒"]
    },

    # ==================== 素菜 ====================
    {
        "name": "蒜蓉西兰花",
        "category": "素菜",
        "subcategory": "叶菜",
        "image": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=400",
        "description": "清爽健康，营养丰富",
        "ingredients": ["西兰花1颗", "蒜末适量", "盐适量", "蚝油1勺"],
        "steps": [
            {"order": 1, "desc": "西兰花掰成小朵，焯水"},
            {"order": 2, "desc": "锅中放油，爆香蒜末"},
            {"order": 3, "desc": "放入西兰花翻炒"},
            {"order": 4, "desc": "加盐、蚝油调味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["健康", "快手", "低卡"]
    },
    {
        "name": "干煸四季豆",
        "category": "素菜",
        "subcategory": "豆制品",
        "image": "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=400",
        "description": "干香入味，口感独特",
        "ingredients": ["四季豆300g", "猪肉末50g", "干辣椒5个", "蒜末适量"],
        "steps": [
            {"order": 1, "desc": "四季豆去筋切段"},
            {"order": 2, "desc": "锅中放油，炸四季豆至表皮起皱"},
            {"order": 3, "desc": "锅留底油，炒肉末至变色"},
            {"order": 4, "desc": "加入干辣椒、蒜末爆香"},
            {"order": 5, "desc": "放入四季豆翻炒，加盐调味"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["下饭", "家常", "快手"]
    },
    {
        "name": "地三鲜",
        "category": "素菜",
        "subcategory": "根茎",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400",
        "description": "东北经典，酱香浓郁",
        "ingredients": ["茄子1个", "土豆1个", "青椒2个", "蒜末适量", "生抽2勺"],
        "steps": [
            {"order": 1, "desc": "茄子、土豆、青椒切滚刀块"},
            {"order": 2, "desc": "锅中放油，分别炸至金黄"},
            {"order": 3, "desc": "锅留底油，爆香蒜末"},
            {"order": 4, "desc": "加入生抽、少许水烧开"},
            {"order": 5, "desc": "放入三种食材翻炒均匀"}
        ],
        "price_hearts": 3,
        "difficulty": "中等",
        "cook_time": "25分钟",
        "tags": ["东北菜", "下饭", "家常"]
    },
    {
        "name": "香菇青菜",
        "category": "素菜",
        "subcategory": "菌菇",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400",
        "description": "清淡爽口，鲜香可口",
        "ingredients": ["青菜300g", "香菇100g", "蒜末适量", "盐适量"],
        "steps": [
            {"order": 1, "desc": "青菜洗净，香菇切片"},
            {"order": 2, "desc": "锅中放油，爆香蒜末"},
            {"order": 3, "desc": "放入香菇翻炒出香味"},
            {"order": 4, "desc": "放入青菜大火快炒"},
            {"order": 5, "desc": "加盐调味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["清淡", "健康", "快手"]
    },
    {
        "name": "酸辣土豆丝",
        "category": "素菜",
        "subcategory": "根茎",
        "image": "https://images.unsplash.com/photo-1518977676601-b53f82ber217?w=400",
        "description": "酸辣开胃，爽脆可口",
        "ingredients": ["土豆2个", "干辣椒5个", "醋2勺", "盐适量", "葱花适量"],
        "steps": [
            {"order": 1, "desc": "土豆切丝，泡水去淀粉"},
            {"order": 2, "desc": "锅中放油，爆香干辣椒"},
            {"order": 3, "desc": "放入土豆丝大火快炒"},
            {"order": 4, "desc": "加入醋、盐翻炒"},
            {"order": 5, "desc": "出锅前撒葱花"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["酸辣", "开胃", "快手"]
    },
    {
        "name": "西红柿炒花菜",
        "category": "素菜",
        "subcategory": "叶菜",
        "image": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400",
        "description": "酸甜可口，营养丰富",
        "ingredients": ["花菜300g", "西红柿2个", "蒜末适量", "盐适量"],
        "steps": [
            {"order": 1, "desc": "花菜掰成小朵焯水，西红柿切块"},
            {"order": 2, "desc": "锅中放油，炒西红柿出汁"},
            {"order": 3, "desc": "放入花菜翻炒"},
            {"order": 4, "desc": "加盐调味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["家常", "健康", "快手"]
    },
    {
        "name": "虎皮青椒",
        "category": "素菜",
        "subcategory": "根茎",
        "image": "https://images.unsplash.com/photo-1583119022894-919a68a3d0e3?w=400",
        "description": "微辣开胃，下饭利器",
        "ingredients": ["青椒8个", "蒜末适量", "生抽1勺", "醋1勺", "糖少许"],
        "steps": [
            {"order": 1, "desc": "青椒去蒂洗净"},
            {"order": 2, "desc": "锅中不放油，干煸青椒至起虎皮"},
            {"order": 3, "desc": "锅中放油，爆香蒜末"},
            {"order": 4, "desc": "放入青椒，加入生抽、醋、糖翻炒"},
            {"order": 5, "desc": "炒至入味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["微辣", "开胃", "下饭"]
    },

    # ==================== 汤羹 ====================
    {
        "name": "番茄蛋花汤",
        "category": "汤羹",
        "subcategory": "蔬菜汤",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "description": "酸甜开胃，营养丰富",
        "ingredients": ["番茄2个", "鸡蛋2个", "葱花适量", "盐适量", "香油少许"],
        "steps": [
            {"order": 1, "desc": "番茄切块，鸡蛋打散"},
            {"order": 2, "desc": "锅中放油，炒番茄出汁"},
            {"order": 3, "desc": "加入适量水烧开"},
            {"order": 4, "desc": "淋入蛋液，轻轻搅拌"},
            {"order": 5, "desc": "加盐调味，撒葱花、淋香油"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["汤类", "清淡", "快手"]
    },
    {
        "name": "紫菜蛋花汤",
        "category": "汤羹",
        "subcategory": "蔬菜汤",
        "image": "https://images.unsplash.com/photo-1603105037880-880cd48d9b04?w=400",
        "description": "简单快手，鲜美可口",
        "ingredients": ["紫菜适量", "鸡蛋1个", "虾皮少许", "葱花适量", "香油少许"],
        "steps": [
            {"order": 1, "desc": "紫菜撕碎，鸡蛋打散"},
            {"order": 2, "desc": "锅中水烧开"},
            {"order": 3, "desc": "放入紫菜、虾皮"},
            {"order": 4, "desc": "淋入蛋液，加盐调味"},
            {"order": 5, "desc": "撒葱花、淋香油即可"}
        ],
        "price_hearts": 1,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["汤类", "快手", "清淡"]
    },
    {
        "name": "冬瓜排骨汤",
        "category": "汤羹",
        "subcategory": "肉汤",
        "image": "https://images.unsplash.com/photo-1607116119750-e7e9e4e9b2ea?w=400",
        "description": "清淡鲜美，消暑解腻",
        "ingredients": ["排骨300g", "冬瓜300g", "姜片3片", "盐适量", "枸杞少许"],
        "steps": [
            {"order": 1, "desc": "排骨焯水，冬瓜切块"},
            {"order": 2, "desc": "锅中放入排骨、姜片，加水烧开"},
            {"order": 3, "desc": "转小火炖30分钟"},
            {"order": 4, "desc": "加入冬瓜继续炖15分钟"},
            {"order": 5, "desc": "加盐调味，撒枸杞即可"}
        ],
        "price_hearts": 4,
        "difficulty": "简单",
        "cook_time": "60分钟",
        "tags": ["汤类", "清淡", "养生"]
    },
    {
        "name": "酸辣汤",
        "category": "汤羹",
        "subcategory": "蔬菜汤",
        "image": "https://images.unsplash.com/photo-1569058242567-93de6f36f8eb?w=400",
        "description": "酸辣开胃，暖身暖胃",
        "ingredients": ["豆腐1块", "木耳适量", "鸡蛋1个", "醋2勺", "胡椒粉1勺"],
        "steps": [
            {"order": 1, "desc": "豆腐切丝，木耳泡发切丝"},
            {"order": 2, "desc": "锅中水烧开，放入豆腐、木耳"},
            {"order": 3, "desc": "加入醋、胡椒粉、生抽调味"},
            {"order": 4, "desc": "淋入蛋液，轻轻搅拌"},
            {"order": 5, "desc": "用水淀粉勾薄芡即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["汤类", "酸辣", "开胃"]
    },

    # ==================== 主食 ====================
    {
        "name": "蛋炒饭",
        "category": "主食",
        "subcategory": "米饭",
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400",
        "description": "粒粒分明，简单美味",
        "ingredients": ["隔夜米饭1碗", "鸡蛋2个", "葱花适量", "盐适量", "酱油少许"],
        "steps": [
            {"order": 1, "desc": "鸡蛋打散，米饭打散"},
            {"order": 2, "desc": "锅中放油，炒鸡蛋至凝固盛出"},
            {"order": 3, "desc": "锅中放油，倒入米饭大火翻炒"},
            {"order": 4, "desc": "加入鸡蛋、盐、少许酱油翻炒"},
            {"order": 5, "desc": "出锅前撒葱花"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["主食", "快手", "家常"]
    },
    {
        "name": "葱油拌面",
        "category": "主食",
        "subcategory": "面条",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400",
        "description": "葱香浓郁，简单好吃",
        "ingredients": ["面条200g", "小葱100g", "生抽3勺", "老抽1勺", "糖1勺"],
        "steps": [
            {"order": 1, "desc": "小葱切段"},
            {"order": 2, "desc": "锅中多放油，小火炸葱至焦黄"},
            {"order": 3, "desc": "加入生抽、老抽、糖调成葱油汁"},
            {"order": 4, "desc": "面条煮熟捞出"},
            {"order": 5, "desc": "浇上葱油汁拌匀即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["主食", "面食", "快手"]
    },
    {
        "name": "饺子",
        "category": "主食",
        "subcategory": "饺子",
        "image": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=400",
        "description": "团圆美满，馅料丰富",
        "ingredients": ["饺子皮500g", "猪肉馅300g", "白菜200g", "葱姜适量", "生抽2勺"],
        "steps": [
            {"order": 1, "desc": "白菜切碎，挤干水分"},
            {"order": 2, "desc": "猪肉馅加白菜、葱姜、生抽拌匀"},
            {"order": 3, "desc": "取饺子皮包入馅料"},
            {"order": 4, "desc": "捏紧边缘"},
            {"order": 5, "desc": "水烧开后下饺子，煮至浮起再煮2分钟"}
        ],
        "price_hearts": 4,
        "difficulty": "困难",
        "cook_time": "60分钟",
        "tags": ["主食", "传统", "团圆"]
    },
    {
        "name": "皮蛋瘦肉粥",
        "category": "主食",
        "subcategory": "粥",
        "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=400",
        "description": "绵密顺滑，营养早餐",
        "ingredients": ["大米100g", "皮蛋2个", "瘦肉100g", "姜丝适量", "葱花适量"],
        "steps": [
            {"order": 1, "desc": "大米洗净，加水大火烧开"},
            {"order": 2, "desc": "转小火熬煮40分钟"},
            {"order": 3, "desc": "瘦肉切丝，加盐、淀粉腌制"},
            {"order": 4, "desc": "皮蛋切丁"},
            {"order": 5, "desc": "粥煮好后加入肉丝、皮蛋煮5分钟"},
            {"order": 6, "desc": "加盐调味，撒葱花即可"}
        ],
        "price_hearts": 3,
        "difficulty": "中等",
        "cook_time": "60分钟",
        "tags": ["早餐", "粥类", "营养"]
    },

    # ==================== 凉菜 ====================
    {
        "name": "拍黄瓜",
        "category": "凉菜",
        "subcategory": "拌菜",
        "image": "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?w=400",
        "description": "爽脆开胃，夏日必备",
        "ingredients": ["黄瓜2根", "蒜末适量", "醋1勺", "生抽1勺", "辣椒油适量"],
        "steps": [
            {"order": 1, "desc": "黄瓜洗净，用刀拍碎切段"},
            {"order": 2, "desc": "蒜切末"},
            {"order": 3, "desc": "加入醋、生抽、辣椒油拌匀"},
            {"order": 4, "desc": "腌制10分钟入味即可"}
        ],
        "price_hearts": 1,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["凉菜", "开胃", "快手"]
    },
    {
        "name": "凉拌木耳",
        "category": "凉菜",
        "subcategory": "拌菜",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400",
        "description": "爽脆可口，营养丰富",
        "ingredients": ["黑木耳200g", "蒜末适量", "醋1勺", "生抽1勺", "辣椒油适量"],
        "steps": [
            {"order": 1, "desc": "木耳泡发，撕成小朵"},
            {"order": 2, "desc": "焯水后捞出过凉水"},
            {"order": 3, "desc": "加入蒜末、醋、生抽、辣椒油拌匀"},
            {"order": 4, "desc": "腌制10分钟入味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "20分钟",
        "tags": ["凉菜", "健康", "爽口"]
    },
    {
        "name": "口水鸡",
        "category": "凉菜",
        "subcategory": "卤味",
        "image": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=400",
        "description": "麻辣鲜香，肉质嫩滑",
        "ingredients": ["鸡腿2个", "花椒油1勺", "辣椒油2勺", "生抽2勺", "花生碎适量"],
        "steps": [
            {"order": 1, "desc": "鸡腿冷水下锅，加姜片煮熟"},
            {"order": 2, "desc": "捞出浸入冰水，让肉质更嫩"},
            {"order": 3, "desc": "调酱汁：花椒油、辣椒油、生抽、蒜末"},
            {"order": 4, "desc": "鸡肉切块摆盘"},
            {"order": 5, "desc": "淋上酱汁，撒花生碎即可"}
        ],
        "price_hearts": 4,
        "difficulty": "中等",
        "cook_time": "30分钟",
        "tags": ["凉菜", "川菜", "麻辣"]
    },

    # ==================== 甜点 ====================
    {
        "name": "芒果班戟",
        "category": "甜点",
        "subcategory": "糕点",
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=400",
        "description": "香甜可口，港式经典",
        "ingredients": ["芒果2个", "低筋面粉80g", "牛奶250ml", "鸡蛋2个", "淡奶油200ml"],
        "steps": [
            {"order": 1, "desc": "鸡蛋、牛奶、面粉混合成面糊"},
            {"order": 2, "desc": "平底锅摊成薄饼"},
            {"order": 3, "desc": "淡奶油打发"},
            {"order": 4, "desc": "芒果切条"},
            {"order": 5, "desc": "薄饼铺上奶油、芒果，包起来即可"}
        ],
        "price_hearts": 4,
        "difficulty": "中等",
        "cook_time": "30分钟",
        "tags": ["甜点", "港式", "芒果"]
    },
    {
        "name": "红豆汤",
        "category": "甜点",
        "subcategory": "糖水",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400",
        "description": "香甜软糯，暖心暖胃",
        "ingredients": ["红豆200g", "冰糖适量", "陈皮少许"],
        "steps": [
            {"order": 1, "desc": "红豆提前泡水4小时"},
            {"order": 2, "desc": "锅中加水，放入红豆大火烧开"},
            {"order": 3, "desc": "转小火煮至红豆软烂"},
            {"order": 4, "desc": "加入冰糖调味"},
            {"order": 5, "desc": "继续煮至糖融化即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "90分钟",
        "tags": ["甜点", "糖水", "养生"]
    },
    {
        "name": "杨枝甘露",
        "category": "甜点",
        "subcategory": "糖水",
        "image": "https://images.unsplash.com/photo-1546173159-315724a31696?w=400",
        "description": "香甜清爽，港式经典",
        "ingredients": ["芒果2个", "西柚1个", "椰浆200ml", "西米50g", "牛奶100ml"],
        "steps": [
            {"order": 1, "desc": "西米煮至透明，过凉水"},
            {"order": 2, "desc": "芒果一半打成泥，一半切丁"},
            {"order": 3, "desc": "西柚剥出果肉"},
            {"order": 4, "desc": "椰浆、牛奶、芒果泥混合"},
            {"order": 5, "desc": "加入西米、芒果丁、西柚即可"}
        ],
        "price_hearts": 3,
        "difficulty": "中等",
        "cook_time": "30分钟",
        "tags": ["甜点", "港式", "清爽"]
    },

    # ==================== 饮品 ====================
    {
        "name": "柠檬蜂蜜水",
        "category": "饮品",
        "subcategory": "果汁",
        "image": "https://images.unsplash.com/photo-1621263764928-df1444c5e859?w=400",
        "description": "酸甜可口，美容养颜",
        "ingredients": ["柠檬1个", "蜂蜜2勺", "温水适量"],
        "steps": [
            {"order": 1, "desc": "柠檬切片"},
            {"order": 2, "desc": "温水中加入蜂蜜搅匀"},
            {"order": 3, "desc": "放入柠檬片即可"}
        ],
        "price_hearts": 1,
        "difficulty": "简单",
        "cook_time": "5分钟",
        "tags": ["饮品", "美容", "简单"]
    },
    {
        "name": "红枣枸杞茶",
        "category": "饮品",
        "subcategory": "茶饮",
        "image": "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=400",
        "description": "补气养血，温暖身心",
        "ingredients": ["红枣10颗", "枸杞1勺", "红糖适量"],
        "steps": [
            {"order": 1, "desc": "红枣洗净，切开去核"},
            {"order": 2, "desc": "锅中加水，放入红枣"},
            {"order": 3, "desc": "大火烧开后转小火煮10分钟"},
            {"order": 4, "desc": "加入枸杞、红糖煮5分钟即可"}
        ],
        "price_hearts": 1,
        "difficulty": "简单",
        "cook_time": "20分钟",
        "tags": ["饮品", "养生", "暖身"]
    },
    {
        "name": "酸梅汤",
        "category": "饮品",
        "subcategory": "果汁",
        "image": "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=400",
        "description": "酸甜解腻，夏日必备",
        "ingredients": ["乌梅50g", "山楂30g", "甘草5g", "冰糖适量", "桂花少许"],
        "steps": [
            {"order": 1, "desc": "乌梅、山楂、甘草洗净"},
            {"order": 2, "desc": "锅中加水，放入所有材料"},
            {"order": 3, "desc": "大火烧开后转小火煮30分钟"},
            {"order": 4, "desc": "加入冰糖调味"},
            {"order": 5, "desc": "过滤后冷藏，喝时撒桂花"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "40分钟",
        "tags": ["饮品", "夏日", "解腻"]
    },
    {
        "name": "豆浆",
        "category": "饮品",
        "subcategory": "果汁",
        "image": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=400",
        "description": "营养早餐，自制健康",
        "ingredients": ["黄豆100g", "水适量", "糖适量"],
        "steps": [
            {"order": 1, "desc": "黄豆提前泡水8小时"},
            {"order": 2, "desc": "放入豆浆机加水"},
            {"order": 3, "desc": "打成豆浆"},
            {"order": 4, "desc": "过滤豆渣，加糖即可"}
        ],
        "price_hearts": 1,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["饮品", "早餐", "营养"]
    },

    # ==================== 更多荤菜 ====================
    {
        "name": "鱼香肉丝",
        "category": "荤菜",
        "subcategory": "猪肉",
        "image": "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=400",
        "description": "酸甜微辣，川菜经典",
        "ingredients": ["猪里脊300g", "木耳50g", "胡萝卜1根", "青椒1个", "豆瓣酱1勺"],
        "steps": [
            {"order": 1, "desc": "猪肉切丝，加料酒、淀粉腌制"},
            {"order": 2, "desc": "木耳、胡萝卜、青椒切丝"},
            {"order": 3, "desc": "调鱼香汁：醋、糖、生抽、淀粉、水混合"},
            {"order": 4, "desc": "锅中放油，炒肉丝至变色盛出"},
            {"order": 5, "desc": "锅中放油，炒豆瓣酱出红油"},
            {"order": 6, "desc": "放入配菜翻炒，倒回肉丝"},
            {"order": 7, "desc": "淋入鱼香汁翻炒均匀即可"}
        ],
        "price_hearts": 4,
        "difficulty": "中等",
        "cook_time": "25分钟",
        "tags": ["川菜", "酸甜", "下饭"]
    },
    {
        "name": "蒜香排骨",
        "category": "荤菜",
        "subcategory": "猪肉",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
        "description": "蒜香四溢，外酥里嫩",
        "ingredients": ["排骨500g", "蒜末50g", "生抽2勺", "料酒1勺", "面包糠适量"],
        "steps": [
            {"order": 1, "desc": "排骨切段，加蒜末、生抽、料酒腌制2小时"},
            {"order": 2, "desc": "排骨裹上淀粉"},
            {"order": 3, "desc": "锅中放油，炸排骨至金黄"},
            {"order": 4, "desc": "锅留底油，炒香蒜末"},
            {"order": 5, "desc": "放入排骨翻炒均匀即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "30分钟",
        "tags": ["蒜香", "炸物", "下酒"]
    },
    {
        "name": "咖喱鸡",
        "category": "荤菜",
        "subcategory": "鸡肉",
        "image": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=400",
        "description": "浓郁咖喱，异域风味",
        "ingredients": ["鸡腿肉400g", "土豆2个", "洋葱1个", "咖喱块3块", "椰浆100ml"],
        "steps": [
            {"order": 1, "desc": "鸡肉切块，土豆、洋葱切块"},
            {"order": 2, "desc": "锅中放油，炒洋葱至透明"},
            {"order": 3, "desc": "加入鸡肉翻炒至变色"},
            {"order": 4, "desc": "加入土豆和适量水炖煮"},
            {"order": 5, "desc": "土豆软烂后加入咖喱块"},
            {"order": 6, "desc": "加入椰浆搅拌均匀即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "40分钟",
        "tags": ["咖喱", "异域", "下饭"]
    },
    {
        "name": "清炒虾仁",
        "category": "荤菜",
        "subcategory": "鱼虾",
        "image": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=400",
        "description": "鲜嫩弹牙，清淡可口",
        "ingredients": ["虾仁300g", "黄瓜1根", "蛋清1个", "淀粉1勺", "姜片适量"],
        "steps": [
            {"order": 1, "desc": "虾仁去虾线，加蛋清、淀粉腌制"},
            {"order": 2, "desc": "黄瓜切丁"},
            {"order": 3, "desc": "锅中放油，滑炒虾仁至变色"},
            {"order": 4, "desc": "加入黄瓜丁翻炒"},
            {"order": 5, "desc": "加盐、料酒调味即可"}
        ],
        "price_hearts": 5,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["海鲜", "清淡", "高蛋白"]
    },
    {
        "name": "酱爆鸡丁",
        "category": "荤菜",
        "subcategory": "鸡肉",
        "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=400",
        "description": "酱香浓郁，快手家常",
        "ingredients": ["鸡胸肉300g", "黄瓜1根", "甜面酱2勺", "料酒1勺", "葱姜适量"],
        "steps": [
            {"order": 1, "desc": "鸡肉切丁，加料酒、淀粉腌制"},
            {"order": 2, "desc": "黄瓜切丁"},
            {"order": 3, "desc": "锅中放油，炒鸡丁至变色"},
            {"order": 4, "desc": "加入甜面酱翻炒出香"},
            {"order": 5, "desc": "放入黄瓜丁翻炒均匀即可"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["酱香", "快手", "家常"]
    },

    # ==================== 更多素菜 ====================
    {
        "name": "醋溜白菜",
        "category": "素菜",
        "subcategory": "叶菜",
        "image": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400",
        "description": "酸爽脆嫩，开胃下饭",
        "ingredients": ["白菜400g", "干辣椒5个", "醋2勺", "生抽1勺", "蒜末适量"],
        "steps": [
            {"order": 1, "desc": "白菜帮和叶分开切"},
            {"order": 2, "desc": "锅中放油，爆香干辣椒和蒜末"},
            {"order": 3, "desc": "先炒白菜帮至断生"},
            {"order": 4, "desc": "加入白菜叶翻炒"},
            {"order": 5, "desc": "淋入醋、生抽翻炒均匀即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["酸辣", "开胃", "快手"]
    },
    {
        "name": "家常豆腐",
        "category": "素菜",
        "subcategory": "豆制品",
        "image": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=400",
        "description": "外焦里嫩，酱香浓郁",
        "ingredients": ["老豆腐1块", "青椒2个", "木耳适量", "生抽2勺", "豆瓣酱1勺"],
        "steps": [
            {"order": 1, "desc": "豆腐切三角块，青椒切块"},
            {"order": 2, "desc": "锅中放油，煎豆腐至两面金黄"},
            {"order": 3, "desc": "锅留底油，炒豆瓣酱出红油"},
            {"order": 4, "desc": "加入木耳、青椒翻炒"},
            {"order": 5, "desc": "放入豆腐，加生抽和少许水炖煮"},
            {"order": 6, "desc": "大火收汁即可"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "20分钟",
        "tags": ["豆腐", "家常", "下饭"]
    },
    {
        "name": "蒜蓉粉丝娃娃菜",
        "category": "素菜",
        "subcategory": "叶菜",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400",
        "description": "蒜香浓郁，清淡鲜美",
        "ingredients": ["娃娃菜2颗", "粉丝1把", "蒜末30g", "生抽2勺", "蚝油1勺"],
        "steps": [
            {"order": 1, "desc": "粉丝泡软，娃娃菜对半切"},
            {"order": 2, "desc": "娃娃菜焯水后摆盘"},
            {"order": 3, "desc": "粉丝铺在娃娃菜上"},
            {"order": 4, "desc": "锅中放油，炒蒜末至金黄"},
            {"order": 5, "desc": "加入生抽、蚝油调成酱汁"},
            {"order": 6, "desc": "浇在粉丝上，蒸8分钟即可"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "20分钟",
        "tags": ["蒸菜", "清淡", "蒜香"]
    },
    {
        "name": "干锅花菜",
        "category": "素菜",
        "subcategory": "叶菜",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400",
        "description": "焦香入味，下饭神器",
        "ingredients": ["花菜300g", "五花肉100g", "干辣椒5个", "蒜末适量", "生抽1勺"],
        "steps": [
            {"order": 1, "desc": "花菜掰小朵，五花肉切片"},
            {"order": 2, "desc": "锅中不放油，干煸花菜至焦黄盛出"},
            {"order": 3, "desc": "锅中放油，煸炒五花肉至出油"},
            {"order": 4, "desc": "加入干辣椒、蒜末爆香"},
            {"order": 5, "desc": "放入花菜翻炒，加生抽调味"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "20分钟",
        "tags": ["干锅", "下饭", "焦香"]
    },

    # ==================== 更多汤羹 ====================
    {
        "name": "玉米排骨汤",
        "category": "汤羹",
        "subcategory": "肉汤",
        "image": "https://images.unsplash.com/photo-1607116119750-e7e9e4e9b2ea?w=400",
        "description": "清甜滋补，营养丰富",
        "ingredients": ["排骨300g", "玉米2根", "胡萝卜1根", "姜片3片", "盐适量"],
        "steps": [
            {"order": 1, "desc": "排骨焯水，玉米切段，胡萝卜切块"},
            {"order": 2, "desc": "锅中放入排骨、姜片，加水烧开"},
            {"order": 3, "desc": "转小火炖30分钟"},
            {"order": 4, "desc": "加入玉米、胡萝卜继续炖20分钟"},
            {"order": 5, "desc": "加盐调味即可"}
        ],
        "price_hearts": 4,
        "difficulty": "简单",
        "cook_time": "60分钟",
        "tags": ["汤类", "滋补", "清甜"]
    },
    {
        "name": "西红柿牛腩汤",
        "category": "汤羹",
        "subcategory": "肉汤",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "description": "酸甜浓郁，肉烂汤鲜",
        "ingredients": ["牛腩500g", "番茄3个", "土豆2个", "姜片3片", "番茄酱2勺"],
        "steps": [
            {"order": 1, "desc": "牛腩切块焯水，番茄切块"},
            {"order": 2, "desc": "锅中放油，炒番茄出汁"},
            {"order": 3, "desc": "加入番茄酱翻炒"},
            {"order": 4, "desc": "放入牛腩、姜片和足量水"},
            {"order": 5, "desc": "大火烧开转小火炖60分钟"},
            {"order": 6, "desc": "加入土豆炖至软烂，加盐调味"}
        ],
        "price_hearts": 6,
        "difficulty": "中等",
        "cook_time": "90分钟",
        "tags": ["汤类", "浓郁", "滋补"]
    },
    {
        "name": "银耳莲子羹",
        "category": "汤羹",
        "subcategory": "糖水",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400",
        "description": "胶质满满，养颜佳品",
        "ingredients": ["银耳1朵", "莲子50g", "红枣10颗", "枸杞适量", "冰糖适量"],
        "steps": [
            {"order": 1, "desc": "银耳泡发撕小朵，莲子去芯"},
            {"order": 2, "desc": "锅中加水，放入银耳大火烧开"},
            {"order": 3, "desc": "转小火煮至银耳出胶"},
            {"order": 4, "desc": "加入莲子、红枣继续煮20分钟"},
            {"order": 5, "desc": "加入枸杞、冰糖煮5分钟即可"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "60分钟",
        "tags": ["甜汤", "养颜", "养生"]
    },

    # ==================== 更多主食 ====================
    {
        "name": "扬州炒饭",
        "category": "主食",
        "subcategory": "米饭",
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400",
        "description": "色彩丰富，粒粒分明",
        "ingredients": ["米饭1碗", "鸡蛋2个", "火腿丁50g", "青豆50g", "虾仁50g"],
        "steps": [
            {"order": 1, "desc": "鸡蛋打散，火腿、青豆、虾仁切丁"},
            {"order": 2, "desc": "锅中放油，炒鸡蛋盛出"},
            {"order": 3, "desc": "锅中放油，炒火腿、青豆、虾仁"},
            {"order": 4, "desc": "加入米饭大火翻炒"},
            {"order": 5, "desc": "加入鸡蛋、盐、葱花翻炒均匀"}
        ],
        "price_hearts": 3,
        "difficulty": "中等",
        "cook_time": "15分钟",
        "tags": ["主食", "炒饭", "丰富"]
    },
    {
        "name": "炸酱面",
        "category": "主食",
        "subcategory": "面条",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400",
        "description": "酱香浓郁，老北京经典",
        "ingredients": ["面条200g", "猪肉馅200g", "甜面酱3勺", "黄瓜丝适量", "豆芽适量"],
        "steps": [
            {"order": 1, "desc": "猪肉馅炒至变色"},
            {"order": 2, "desc": "加入甜面酱小火炒出香味"},
            {"order": 3, "desc": "加入少许水煮至浓稠"},
            {"order": 4, "desc": "面条煮熟捞出"},
            {"order": 5, "desc": "浇上炸酱，配黄瓜丝、豆芽即可"}
        ],
        "price_hearts": 3,
        "difficulty": "中等",
        "cook_time": "20分钟",
        "tags": ["主食", "面食", "北京"]
    },
    {
        "name": "小笼包",
        "category": "主食",
        "subcategory": "面点",
        "image": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=400",
        "description": "皮薄汁多，上海名点",
        "ingredients": ["面粉300g", "猪肉馅300g", "皮冻100g", "生抽2勺", "姜末适量"],
        "steps": [
            {"order": 1, "desc": "面粉加温水揉成光滑面团"},
            {"order": 2, "desc": "猪肉馅加皮冻、生抽、姜末拌匀"},
            {"order": 3, "desc": "面团擀成薄皮，包入馅料"},
            {"order": 4, "desc": "捏出褶子，收口"},
            {"order": 5, "desc": "蒸锅水烧开，蒸8-10分钟即可"}
        ],
        "price_hearts": 4,
        "difficulty": "困难",
        "cook_time": "60分钟",
        "tags": ["主食", "面点", "上海"]
    },
    {
        "name": "南瓜粥",
        "category": "主食",
        "subcategory": "粥",
        "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=400",
        "description": "香甜绵密，营养早餐",
        "ingredients": ["南瓜300g", "大米100g", "冰糖适量"],
        "steps": [
            {"order": 1, "desc": "南瓜去皮切块，大米洗净"},
            {"order": 2, "desc": "大米加水大火烧开"},
            {"order": 3, "desc": "加入南瓜块转小火煮"},
            {"order": 4, "desc": "煮至南瓜软烂，用勺压碎"},
            {"order": 5, "desc": "加入冰糖煮至融化即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "40分钟",
        "tags": ["早餐", "粥类", "养胃"]
    },

    # ==================== 更多凉菜 ====================
    {
        "name": "凉拌海带丝",
        "category": "凉菜",
        "subcategory": "拌菜",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400",
        "description": "爽脆可口，碘含量高",
        "ingredients": ["海带丝300g", "蒜末适量", "醋2勺", "生抽1勺", "辣椒油适量"],
        "steps": [
            {"order": 1, "desc": "海带丝焯水后捞出过凉水"},
            {"order": 2, "desc": "加入蒜末、醋、生抽"},
            {"order": 3, "desc": "淋上辣椒油拌匀"},
            {"order": 4, "desc": "腌制10分钟入味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["凉菜", "海带", "爽口"]
    },
    {
        "name": "夫妻肺片",
        "category": "凉菜",
        "subcategory": "卤味",
        "image": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=400",
        "description": "麻辣鲜香，川菜经典",
        "ingredients": ["牛肉200g", "牛杂200g", "花椒油1勺", "辣椒油2勺", "花生碎适量"],
        "steps": [
            {"order": 1, "desc": "牛肉、牛杂卤熟"},
            {"order": 2, "desc": "捞出放凉后切薄片"},
            {"order": 3, "desc": "调酱汁：花椒油、辣椒油、生抽、蒜末"},
            {"order": 4, "desc": "肉片摆盘，淋上酱汁"},
            {"order": 5, "desc": "撒上花生碎、香菜即可"}
        ],
        "price_hearts": 5,
        "difficulty": "中等",
        "cook_time": "60分钟",
        "tags": ["凉菜", "川菜", "麻辣"]
    },
    {
        "name": "蒜泥白肉",
        "category": "凉菜",
        "subcategory": "卤味",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
        "description": "蒜香浓郁，肥而不腻",
        "ingredients": ["五花肉300g", "蒜泥30g", "生抽2勺", "辣椒油1勺", "黄瓜丝适量"],
        "steps": [
            {"order": 1, "desc": "五花肉整块煮熟"},
            {"order": 2, "desc": "捞出放凉后切薄片"},
            {"order": 3, "desc": "调蒜泥汁：蒜泥、生抽、辣椒油、醋"},
            {"order": 4, "desc": "黄瓜丝垫底，肉片摆盘"},
            {"order": 5, "desc": "淋上蒜泥汁即可"}
        ],
        "price_hearts": 4,
        "difficulty": "中等",
        "cook_time": "40分钟",
        "tags": ["凉菜", "蒜香", "下酒"]
    },

    # ==================== 更多甜点 ====================
    {
        "name": "双皮奶",
        "category": "甜点",
        "subcategory": "糖水",
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=400",
        "description": "香滑细腻，甜而不腻",
        "ingredients": ["全脂牛奶500ml", "蛋清2个", "糖2勺", "红豆适量"],
        "steps": [
            {"order": 1, "desc": "牛奶加热后倒入碗中，冷却后形成奶皮"},
            {"order": 2, "desc": "蛋清加糖打散"},
            {"order": 3, "desc": "倒出牛奶，留奶皮在碗底"},
            {"order": 4, "desc": "牛奶与蛋清混合后倒回碗中"},
            {"order": 5, "desc": "蒸15分钟，冷却后放红豆即可"}
        ],
        "price_hearts": 3,
        "difficulty": "中等",
        "cook_time": "30分钟",
        "tags": ["甜点", "港式", "奶香"]
    },
    {
        "name": "蛋挞",
        "category": "甜点",
        "subcategory": "糕点",
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=400",
        "description": "酥脆香甜，葡式经典",
        "ingredients": ["蛋挞皮12个", "鸡蛋2个", "牛奶150ml", "糖30g", "淡奶油50ml"],
        "steps": [
            {"order": 1, "desc": "鸡蛋、牛奶、糖、淡奶油混合搅匀"},
            {"order": 2, "desc": "过滤蛋液"},
            {"order": 3, "desc": "蛋挞皮摆入烤盘"},
            {"order": 4, "desc": "倒入蛋液至八分满"},
            {"order": 5, "desc": "烤箱200度烤20分钟至金黄"}
        ],
        "price_hearts": 3,
        "difficulty": "简单",
        "cook_time": "30分钟",
        "tags": ["甜点", "烘焙", "葡式"]
    },
    {
        "name": "绿豆汤",
        "category": "甜点",
        "subcategory": "糖水",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400",
        "description": "清热解暑，夏日必备",
        "ingredients": ["绿豆200g", "冰糖适量", "百合少许"],
        "steps": [
            {"order": 1, "desc": "绿豆提前泡水2小时"},
            {"order": 2, "desc": "锅中加水，放入绿豆大火烧开"},
            {"order": 3, "desc": "转小火煮至绿豆开花"},
            {"order": 4, "desc": "加入百合煮10分钟"},
            {"order": 5, "desc": "加入冰糖调味即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "60分钟",
        "tags": ["甜点", "消暑", "夏日"]
    },

    # ==================== 更多饮品 ====================
    {
        "name": "西瓜汁",
        "category": "饮品",
        "subcategory": "果汁",
        "image": "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=400",
        "description": "清甜解渴，夏日必备",
        "ingredients": ["西瓜500g", "冰块适量", "柠檬汁少许"],
        "steps": [
            {"order": 1, "desc": "西瓜去籽切块"},
            {"order": 2, "desc": "放入榨汁机打成汁"},
            {"order": 3, "desc": "过滤后加入冰块"},
            {"order": 4, "desc": "挤少许柠檬汁即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["饮品", "夏日", "解渴"]
    },
    {
        "name": "姜撞奶",
        "category": "饮品",
        "subcategory": "奶饮",
        "image": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=400",
        "description": "辛辣暖胃，广式甜品",
        "ingredients": ["全脂牛奶250ml", "老姜30g", "糖2勺"],
        "steps": [
            {"order": 1, "desc": "老姜去皮磨成姜蓉，挤出姜汁"},
            {"order": 2, "desc": "姜汁倒入碗中"},
            {"order": 3, "desc": "牛奶加糖加热至70度"},
            {"order": 4, "desc": "将牛奶快速冲入姜汁中"},
            {"order": 5, "desc": "静置5分钟凝固即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "15分钟",
        "tags": ["饮品", "广式", "暖胃"]
    },
    {
        "name": "桂花酒酿",
        "category": "饮品",
        "subcategory": "酒饮",
        "image": "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=400",
        "description": "香甜温润，微醺怡人",
        "ingredients": ["酒酿200g", "桂花1勺", "枸杞适量", "鸡蛋1个", "冰糖适量"],
        "steps": [
            {"order": 1, "desc": "锅中加水烧开"},
            {"order": 2, "desc": "加入酒酿搅散"},
            {"order": 3, "desc": "打入鸡蛋搅成蛋花"},
            {"order": 4, "desc": "加入枸杞、冰糖煮2分钟"},
            {"order": 5, "desc": "出锅撒上桂花即可"}
        ],
        "price_hearts": 2,
        "difficulty": "简单",
        "cook_time": "10分钟",
        "tags": ["饮品", "酒酿", "微醺"]
    },
]


async def seed_database():
    """
    初始化种子数据

    将预设的分类和菜谱数据导入数据库。
    如果数据库已有数据则跳过。
    """
    # 检查是否已有数据
    category_count = await categories_collection.count_documents({})
    if category_count > 0:
        print(f"数据库已有 {category_count} 个分类，跳过初始化")
        return

    print("开始导入种子数据...")

    # 导入分类
    await categories_collection.insert_many(CATEGORIES)
    print(f"已导入 {len(CATEGORIES)} 个分类")

    # 导入菜谱
    for recipe in RECIPES:
        recipe["created_at"] = datetime.now()
    await recipes_collection.insert_many(RECIPES)
    print(f"已导入 {len(RECIPES)} 道菜谱")

    print("种子数据导入完成！")
