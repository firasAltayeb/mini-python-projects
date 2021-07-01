open_list = ["[", "{", "(", "（", "【", "｛", "「"]
close_list = ["]", "}", ")", "）", "】", "｝", "」"]

kana_List = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよら" \
            "りるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽっゃゅょアイウ" \
            "エオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレ" \
            "ロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョァィェォ、。「" \
            "」）｛｝”：；～！"

latin_characters = "abcdefghijklmnopqrstuvwxyz1234567890" \
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ,./;'[]()*&^^%"

jlpt_n5_characters = "一七万三上下中九二五人今休何先入八六円出前北十千午半南友右名四国土外大天女子学小山川左年後日時書月木本来" \
                     "東校母毎気水火父生男白百聞行西見話語読車金長間雨電食高"

jlpt_n4_characters = "不世主事京仕代以会住体作使借元兄公写冬切別力勉動医去口古台同味品員問図地堂場売夏夕多夜妹姉始字安室家少屋" \
                     "工帰広店度建弟強待心思急悪意手持教文料新方旅族早明映春昼曜有服朝業楽歌止正歩死注洋海漢牛物特犬理用田町画" \
                     "界病発目真着知研社私秋究空立答紙終習考者肉自色花英茶親言計試買貸質赤走起足転近送通週運道重野銀開院集青音" \
                     "題風飯飲館駅験魚鳥黒"

jlpt_n3_characters = "偉頂偶到居抱歳疲髪与両乗予争互亡交他付件任伝似位余例供便係信倒候値側備働優光全共具内冷処列初判利制刻割加助努" \
                     "労務勝勤化単危原参反収取受号合向君否吸吹告呼命和商喜回因困園在報増声変夢太夫失好妻娘婚婦存宅守完官定実客害容" \
                     "宿寄富寒寝察対局差市師席常平幸幾座庭式引当形役彼徒得御必忘忙念怒怖性恐恥息悲情想愛感慣成戦戻所才打払投折抜押" \
                     "招指捕掛探支放政敗散数断易昔昨晩景晴暗暮曲更最望期未末束杯果格構様権横機欠次欲歯残段殺民求決治法泳洗活流浮消" \
                     "深済渡港満演点然煙熱犯状猫王現球産由申留番疑痛登皆盗直相眠石破確示礼祖神福科程種積突窓笑等箱米精約組経給絵絶" \
                     "続緒罪置美老耳職育背能腹舞船良若苦草落葉薬術表要規覚観解記訪許認誤説調談論識警議負財貧責費資賛越路辞込迎返迷" \
                     "追退逃途速連進遅遊過達違遠適選部都配酒閉関降限除険陽際雑難雪静非面靴頭頼顔願類飛首馬鳴"

jlpt_n2_characters = "膚召挟枯沸濯燥瓶耕肯脂踊軒軟郊隅隻傾刊咲塗帽憎溶滴灯畜畳賢伺刷包匹双叫塔封床掘損曇柔沈泊涙涼湿炭珍硬磨筒籍粒" \
                     "綿績缶肌舟荒衣袋誌講辛鈍鉱零並丸久乱乳乾了介仏令仲伸低依個倍停像億兆児党兵冊再凍券刺則副劇効勇募勢区卒協占印" \
                     "卵厚史各含周喫営団囲固圧坂均型埋城域塩境央奥姓委季孫宇宝寺専将尊導届層岩岸島州巨巻布希帯幅干幼庁底府庫延弱律" \
                     "復快恋患悩戸承技担拝拾捜捨掃採接換改敬旧昇星普暴替札机材村板林枚枝柱査栄根械棒森植極橋欧武歴殿毒比毛氷永汗汚" \
                     "池河油況泉波泥浅浴液混清減温測湖湯湾準漁濃灰焼照燃爆片版玉甘略療皮皿省県短砂祈祝祭禁秒移税章童競竹符筆算管築" \
                     "簡粉糸紅純細紹絡総緑線編練署群羽翌肩胃胸脳腕腰臓臣航般芸荷菓菜著蒸蔵薄虫血被装裏補複角触訓設詞詰課諸谷豊象貝" \
                     "貨販貯貿賞贈超跡軍軽輪輸農辺述逆造郵量針鉄銅鋭録門防陸階雇雲震革順預領額香駐骨麦黄鼻齢"

jlpt_n1_characters = "且丹之乙亜享伏伐佳侮俸倹傍傑冠准凌凝凡凸凹剖剰劾勲匠匿升卑卸叔叙吟呈呉哉唄啓喝嘉嘱囚坑坪堕堪壌奉奔妄姻婿媒宰" \
                     "寂寛寡尉尚尿屯岬峠峡崇帆帥庶庸廉弊弔弥弦徐循忌恭悠悦悼惜惨愉愚慕慨慶憂憤憧憾戯扶披抹拍拐拙拷据搭搾摂擬敢旋旦" \
                     "昌智暁曙曹朴朽杏某栓栞栽桟梓椎楓槽欄款殉殻汰沙泌洪浄浪淑渓湧漆漬漸濁煩猶瑛瑞瑠璃甚畔疎疾痢痴癒盲睦矯硫碑礁禍" \
                     "稿穀窃窒窮篤粗粛紋紡累紳紺絹綾緋緯縛縫繊罷羅肖胆胎胞胡腸膜舗舶艇茎茜荘莉萌葵蒼藍藩藻虐虜蛮蝶衡詠該諒諭謡謹譜" \
                     "賊賓赦赴践轄迭逝逸遍遥遮遷遼那郭酌酪酬酵酷醜醸鋳錠錦錯鎌鎮閑閲阿陪陵随雌靖顕飽駿騰髄鯉鯨鶏鼓乃倫偏呂唆噴孤怠" \
                     "恒惰慢擁殊没牲猟祥秩糧膨芳覇貫賠輔遇遭鎖陥陳隼須颯亮喚堤塚媛慈浦渦玄聡肪苗蓮襟貞邸郡釈亭仰伯俗刈剛劣勘后唯墳" \
                     "壇壮奨奮妃尼峰巧廷彰征悟把抽拓拘搬敏晶枠桑概殖洞浸涯淡漂漫潤煮猿珠疫礎簿紫繁翻衰覆訂誉誓諮謀軌邪銘陛陶隔駄駒" \
                     "鶴伊伴佐哀唇培塀墜如婆尺尽帳幣彩恨悔慎憩憶扇扉挿掌斜柳欺歓殴炊爽班盾瞭祉稲穫耐胴脅蓄虹蚊蛇詐輝辱迅遂鉢霜霧飢" \
                     "餓騎麻丘也井仁侍侵俵偽儀克凶刃剤卓即吉哲喪垣堅塊塾墨姫威娯嫁嬢孔寧寮寸岳嵐帝幽庄弧徹忍慰懇懲拒拠括拳挑措揚握" \
                     "揺摩撤撲擦斉斎斗旨昭暦暫朗朱析枢架柄桃梨棄棚棟樹沼泡泰溝滅滋滑滝潜潟潮澄瀬炉焦牧狂狩琴甲癖盆眺瞬瞳矛砕砲碁租" \
                     "称稼穂穏竜範粘糾紛綱網縁翔翼肝脚至艦芝芽菊菌虎蛍裂裸襲誇誠貢趣距軸較遺郷釣錬鍛鐘鑑阻陰隆雷霊露顧魂魔鳩黙丁乏" \
                     "亀仙仮企伎併価促俊保修俳倉健偵傘催債傷僕僚僧償充免典兼冒冗刀刑削剣創功励勧博却厄厳又及句司吐唱善嘆器圏垂執基" \
                     "堀塁墓壁壊士奇奈奏契奪奴妊妙妥妨姿娠嫌嬉宗宙宜宣宮宴密審射尋就尾屈展属履岐崎崩巡巣己幕幹幻序康廃廊弁弓張弾彫" \
                     "影往径従微徳徴志応忠怪恩恵惑態慮憲懐懸我戒房扱批抑抗択抵拡挙振授排控推掲描提揮援携摘撃撮操攻故救整敵敷斐斤施" \
                     "旗既旬昆是暇暑暖杉条松染株核案桜梅棋検標模氏汁江汽沖沢沿泣津派浜添渇渉渋源滞漏漠潔激災炎為烈熊熟犠独狭猛献獄" \
                     "獣獲率環異症皇益盛盟監盤眉看眼睡督矢磁票禅秀秘稚穴端笛第筋策節粋糖系紀納級素索結絞統継維綺緊締緩縄縦縮織繰罰" \
                     "羊義聖聴肥肺脈脱腐臨臭致興舌舎芋茂華葬薦藤虚融衆街衛衝裁裕製褒視覧討託訟訳訴診証評詩詳誕誘請諾謙謝譲護豆豚豪" \
                     "貴賀賃賄購跳踏躍載輩迫透逮遣避還邦郎酔酢酸鈴鉛銃銭鋼鏡閣閥闘陣隊障隠隣隷雄雅離雰需響項頑頻飼飾養駆騒驚鬼魅鮮" \
                     "鹿麗丑丙丞亘亥亦亨伍伶伽但佑侃侑侯倖倣倭偲儒允冴冶凜凪凱勁勅勺匁匡卯厘叡只叶吏啄喬嗣嚇圭塑墾壱奎嫡孟宏宥宵寅" \
                     "尭峻崚嵩嵯嶺巌巳巴巽弐弘彗彦彪彬怜恕悌惇惟惣愁慧抄捷捺敦斥於旭旺昂昴晃晋晏晟晨暉暢朋朔朕李杜柊柚柾栗桂桐梢梧" \
                     "棺椋椰椿楊楠楼榛槙槻樺橘檀欣欽毅毬汐洲洵洸浩淳渚渥滉漱澪濫熙燎燦燿爵爾猪玖玲琉琢琳瑚瑳瑶甫畝痘皐皓眸硝碧碩磯" \
                     "祐禄禎秦稀稔稜穣窯竣笙笹箇紗紘紬絃絢綜綸繕繭翁翠耀耗耶肇肢胤脩脹舜艶芙芹苑茄茅茉莞菖菫萩蒔蓉蔦蕉蕗薪薫蘭虞蚕" \
                     "衷衿袈裟褐詔詢誼諄謁謄賜賦赳辰迪逐逓遵邑郁酉采銑錘附雛霞鞠韻頌頒馨魁鮎鯛鳳鴻鵬鷹麟麿黎黛"

filtered_kanji = "一二三四五六七八九十口日月田目古吾明品呂早世旦丨旧丶自白百中千舌升丸寸専博卜占上下朝ハ貝員儿見児元" \
                 "頁頑几凡勹負万句勺的首乙乱直具真工ナ左右有刀刃切召昭則別丁町可頂子了女好母兄小少大夕多外名厂石肖砕" \
                 "砂光太器妙省奇川州順水永泉原願源活消泊土圭寺時火炎点照魚里黒量埋冂同向宀字守完安宮寄畐富木林森植村" \
                 "相本案未末味妹朱艹若草苦薄葉莫暮苗兆眺犬状黙然牛特告先洗介界茶合王玉現狂呈全理主注金道造迫逃辺車連" \
                 "前夂各格略客額夏処条落冖軍運夢亠高京景舎周週士吉壮売学覚聿書津攵攻敗枚故敬言警計詰話語読調談弋式試" \
                 "戈或域戊成城戌威滅減銭浅止歩歴武正証政定走超越是題廴建衣装裏哀遠初巾布幕市姉帯刺制云転芸雨雲冫冬天" \
                 "泣妾章商啇適敵匕頃北背比皆旨毎梅海复腹欠吹歌次資姿音暗識竟鏡境亡荒望方坊訪放激兑脱説曽喬橋立増東壬" \
                 "廷染歳県也地池虫独風己起改記包亀電豕遂家昜場湯羊美洋詳達差着隹唯誰焦集進雑準奪確午許権観羽習翌曜困" \
                 "固国団因園回广店庫庭床心忘忍認志誌忠思応意想息恐惑感憂忙怖悔憎憶必手我義議扌抱批打捨指持推提担拠描" \
                 "接掛开研鼻刑型才存在乃及吸扱丈史吏更又隻護奴怒友抜殳投設撃支技圣怪軽叔寂反坂板返爪浮将受愛厶払広弁" \
                 "雄台治始去法会至室到致互育充流出山崩密入込分貧公谷容欲堂常皮波破被歹残殊列死舛瞬耳取趣最恥職聖聴懐" \
                 "買置環夫規失鉄臣巨力男労勧努加行復得従徒待彼役徳微街禾程和移秋私秘称利香秀米迷奥数類膝様求竹笑肋筋" \
                 "箱筆等算答人佐住位仲体件仕他伏伝仏休仮俗信例個健側値倒僧儀催侮使便優宿傷保付府任代化花傾何荷傍俺咅" \
                 "倍久内丙柄肉从坐座以似善年夜遊旅勿物易尸屋握屈居層局遅尺尽沢訳昼戸肩戻涙示礼福社視宗祭察由油甲押申" \
                 "伸神果斤所近折哲暫断質乍昨作ヨ雪尋急寝婦当争事尹伊君群耐端両満凵画曲斗料科図用備昔借惜散廿席度渡卉" \
                 "尭焼半判巻勝藤片版之芝不否杯矢族知智矛務帰引弘強弱弗第弟丂号汚与写身射謝老考孝教者著暑諸頬𠂤追師官" \
                 "父交効較校足距路踏骨咼過阝際障隙随陽防院隊降階隣隠穴空窓突究兀探深丘兵糸織線緒続絵統給結終級紅納経" \
                 "約細総継縁緊幺後幾機玄系係卩却脚卸御服命令冷領勇通疋疑巳犯危腕卵留印臼興酉酒酷酔配尊豆頭短豊壴喜樹" \
                 "皿血温盛艮銀根即節退限眼良娘食飯飲館養既概平呼評メ希凶胸離殺屯純辛辞辟壁新親幸報丩叫収陸勢熱亥刻述" \
                 "術寒㐮毒素青精情晴清静責積表害割生星姓性産春実奉棒堇勤難乗今含念陰予野兼嫌西価要腰煙南門問間闇簡開" \
                 "閉聞倉創非悲罪輩ユ侯喉決快韋偉違衛干軒岸于余途束頼速整剣重動働種疒病疲痛癖匚医匹区抑仰迎癶登発彡形" \
                 "影彦顔参修珍文対斉済楽薬央英映赤変跡恋黄横巴色絶甘其期基甚堪貴遺遣舞無且組助並普霊業僕共供異暴選殿" \
                 "井囲亜悪円角触解再冓講構冊論輪氏紙婚低底民眠甫捕都那郷響郎部派衆段舟般船益暇敷来気飛沈妻凄面声呉承" \
                 "極牙邪釆番毛尾宅為長張髪展単戦脳悩厳挙鳥鳴島隅逆就免晩勉象像馬験駅騒駄驚虎虚戯慮劇鹿麗能態寅演辰振" \
                 "農关送関鬼魂魔"

jouyou_kanji = "一九七二人入八力十下三千上口土夕大女子小山川五天中六円手文日月木水火犬王正出本右四左玉生田白目石立百" \
               "年休先名字早気竹糸耳虫村男町花見貝赤足車学林空金雨青草音校森刀万丸才工弓内午少元今公分切友太引心戸方" \
               "止毛父牛半市北古台兄冬外広母用矢交会合同回寺地多光当毎池米羽考肉自色行西来何作体弟図声売形汽社角言谷" \
               "走近里麦画東京夜直国姉妹岩店明歩知長門昼前南点室後春星海活思科秋茶計風食首夏弱原家帰時紙書記通馬高強" \
               "教理細組船週野雪魚鳥黄黒場晴答絵買朝道番間雲園数新楽話遠電鳴歌算語読聞線親頭曜顔丁予化区反央平申世由" \
               "氷主仕他代写号去打皮皿礼両曲向州全次安守式死列羊有血住助医君坂局役投対決究豆身返表事育使命急指持拾昭" \
               "相味幸始実定岸所放昔板泳注波油受物具委和者取服苦重乗係品客県屋炭度待柱洋畑界発研神秒級美負送追面島勉" \
               "倍真員宮庫庭旅根酒消流病息荷起速配院悪商動宿帳族深球祭第笛終習転進都部問章寒暑植温湖港湯登短童等筆着" \
               "期勝葉落軽運遊開階陽集悲飲歯業感想暗漢福詩路農鉄意様緑練銀駅鼻横箱談調橋整薬館題士不夫欠氏民史必失包" \
               "末未以付令加司功札辺印争仲伝共兆各好成灯老衣求束兵位低児冷別努労告囲完改希折材利臣良芸初果刷卒念例典" \
               "周協参固官底府径松毒泣治法牧的季英芽単省変信便軍勇型建昨栄浅胃祝紀約要飛候借倉孫案害帯席徒挙梅残殺浴" \
               "特笑粉料差脈航訓連郡巣健側停副唱堂康得救械清望産菜票貨敗陸博喜順街散景最量満焼然無給結覚象貯費達隊飯" \
               "働塩戦極照愛節続置腸辞試歴察旗漁種管説関静億器賞標熱養課輪選機積録観類験願鏡競議久仏支比可旧永句圧弁" \
               "序快技状防武承価舎券制効妻居往性招易枝河版肥述非保厚故布刊犯示再仮件任因団在舌似余判均志条災応政査独" \
               "祖則逆退迷限師個修俵益能容恩格桜留破素耕財造率貧基婦寄常張術情採授接断液混現略眼務移経規許設責険備営" \
               "報富属復提検減測税程絶統証評賀貸貿過勢幹準損禁罪義群墓夢解豊資鉱預飼像境増徳慣態構演精総綿製複適酸銭" \
               "銅際雑領導敵暴潔確編賛質興衛燃築輸績講謝織職額識護亡寸己干仁尺片冊収処幼庁穴危后灰吸存宇宅机至否我系" \
               "卵忘孝困批私乱垂乳供並刻呼宗宙宝届延忠拡担拝枚沿若看城奏姿宣専巻律映染段洗派皇泉砂紅背肺革蚕値俳党展" \
               "座従株将班秘純納胸朗討射針降除陛骨域密捨推探済異盛視窓翌脳著訪訳欲郷郵閉頂就善尊割創勤裁揮敬晩棒痛筋" \
               "策衆装補詞貴裏傷暖源聖盟絹署腹蒸幕誠賃疑層模穀磁暮誤誌認閣障劇権潮熟蔵諸誕論遺奮憲操樹激糖縦鋼厳優縮" \
               "覧簡臨難臓警乙了又与及丈刃凡勺互弔井升丹乏匁屯介冗凶刈匹厄双孔幻斗斤且丙甲凸丘斥仙凹召巨占囚奴尼巧払" \
               "汁玄甘矛込弐朱吏劣充妄企仰伐伏刑旬旨匠叫吐吉如妃尽帆忙扱朽朴汚汗江壮缶肌舟芋芝巡迅亜更寿励含佐伺伸但" \
               "伯伴呉克却吟吹呈壱坑坊妊妨妙肖尿尾岐攻忌床廷忍戒戻抗抄択把抜扶抑杉沖沢沈没妥狂秀肝即芳辛迎邦岳奉享盲" \
               "依佳侍侮併免刺劾卓叔坪奇奔姓宜尚屈岬弦征彼怪怖肩房押拐拒拠拘拙拓抽抵拍披抱抹昆昇枢析杯枠欧肯殴況沼泥" \
               "泊泌沸泡炎炊炉邪祈祉突肢肪到茎苗茂迭迫邸阻附斉甚帥衷幽為盾卑哀亭帝侯俊侵促俗盆冠削勅貞卸厘怠叙咲垣契" \
               "姻孤封峡峠弧悔恒恨怒威括挟拷挑施是冒架枯柄柳皆洪浄津洞牲狭狩珍某疫柔砕窃糾耐胎胆胞臭荒荘虐訂赴軌逃郊" \
               "郎香剛衰畝恋倹倒倣俸倫翁兼准凍剣剖脅匿栽索桑唆哲埋娯娠姫娘宴宰宵峰貢唐徐悦恐恭恵悟悩扇振捜挿捕敏核桟" \
               "栓桃殊殉浦浸泰浜浮涙浪烈畜珠畔疾症疲眠砲祥称租秩粋紛紡紋耗恥脂朕胴致般既華蚊被託軒辱唇逝逐逓途透酌陥" \
               "陣隻飢鬼剤竜粛尉彫偽偶偵偏剰勘乾喝啓唯執培堀婚婆寂崎崇崩庶庸彩患惨惜悼悠掛掘掲控据措掃排描斜旋曹殻貫" \
               "涯渇渓渋淑渉淡添涼猫猛猟瓶累盗眺窒符粗粘粒紺紹紳脚脱豚舶菓菊菌虚蛍蛇袋訟販赦軟逸逮郭酔釈釣陰陳陶陪隆" \
               "陵麻斎喪奥蛮偉傘傍普喚喫圏堪堅堕塚堤塔塀媒婿掌項幅帽幾廃廊弾尋御循慌惰愉惑雇扉握援換搭揚揺敢暁晶替棺" \
               "棋棚棟款欺殖渦滋湿渡湾煮猶琴畳塁疎痘痢硬硝硫筒粧絞紫絡脹腕葬募裕裂詠詐詔診訴越超距軸遇遂遅遍酢鈍閑隅" \
               "随焦雄雰殿棄傾傑債催僧慈勧載嗣嘆塊塑塗奨嫁嫌寛寝廉微慨愚愁慎携搾摂搬暇楼歳滑溝滞滝漠滅溶煙煩雅猿献痴" \
               "睡督碁禍禅稚継腰艇蓄虞虜褐裸触該詰誇詳誉賊賄跡践跳較違遣酬酪鉛鉢鈴隔雷零靴頑頒飾飽鼓豪僕僚暦塾奪嫡寡" \
               "寧腐彰徴憎慢摘概雌漆漸漬滴漂漫漏獄碑稲端箇維綱緒網罰膜慕誓誘踊遮遭酵酷銃銑銘閥隠需駆駄髪魂錬緯韻影鋭" \
               "謁閲縁憶穏稼餓壊懐嚇獲穫潟轄憾歓環監緩艦還鑑輝騎儀戯擬犠窮矯響驚凝緊襟謹繰勲薫慶憩鶏鯨撃懸謙賢顕顧稿" \
               "衡購墾懇鎖錯撮擦暫諮賜璽爵趣儒襲醜獣瞬潤遵償礁衝鐘壌嬢譲醸錠嘱審薪震錘髄澄瀬請籍潜繊薦遷鮮繕礎槽燥藻" \
               "霜騒贈濯濁諾鍛壇鋳駐懲聴鎮墜締徹撤謄踏騰闘篤曇縄濃覇輩賠薄爆縛繁藩範盤罷避賓頻敷膚譜賦舞覆噴墳憤幣弊" \
               "壁癖舗穂簿縫褒膨謀墨撲翻摩磨魔繭魅霧黙躍癒諭憂融慰窯謡翼羅頼欄濫履離慮寮療糧隣隷霊麗齢擁露"
