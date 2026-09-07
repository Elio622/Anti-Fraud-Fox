# game/ch09.rpy
#
# 关卡9：冒充公检法诈骗（假警官电话 + 安全账户骗局）
#
# 本关专属角色：骗子冒充的「李警官」（复用诈骗犯浣熊的立绘）。
define l9_cop = Character("李警官", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="fraud")

define l9_tip = "公检法不会电话办案，安全账户是谎言，通缉令不会网上发，九六一一零来咨询！"


label ch9:

    # === 前置剧情 ===
    scene bg_living
    n "周四傍晚，爸爸妈妈还没下班，阿狐独自在家写作业。妈妈手机突然响起，来电显示一串陌生号码。"
    n "阿狐帮妈妈接起电话。"
    l9_cop serious "你好，我是市公安局刑侦大队李警官，警号072156。你的手机卡涉嫌一起特大洗钱案，现在需要你配合调查！"
    think confused "洗钱？我只是个小学生呀……可对方连警号都报了，听起来好正经……"

    # === 第一轮抉择 ===
    l9_cop serious "根据法律规定，涉嫌人员必须配合调查，泄露案情要负法律责任！你叫什么名字？家里大人做什么工作的？"

    menu:
        "想起老师的提醒，立刻挂断电话":
            jump ch9_A
        "又害怕又好奇，追问到底是什么案子":
            jump ch9_B
        "不敢怠慢，老老实实回答问题":
            jump ch9_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch9_A:
    scene bg_living
    n "「洗钱案」三个字听得阿狐心跳加速，但他猛然想起老师反诈课上的话。"
    think serious "老师说过：公检法机关绝不会打电话办案，更不会让老百姓转账！这是骗局！"
    mc serious "警察叔叔不会打电话让我配合调查，你是假的，我挂了！"
    n "阿狐挂断电话，把陌生号码拉黑，并第一时间给妈妈打电话说明情况。"
    mom serious "做得对！妈妈马上拨打96110反诈专线核实——这类号码正是诈骗电话，妈一会儿就把骚扰拦截打开。"

    scene bg_bedroom
    police laugh "反应非常快！真警察办案会当面出示证件、做笔录，绝不会电话里要求转账或「配合调查」。陌生电话谈案件，一律先挂断！"

    $ clear_chapter(9, 3)
    $ quick_menu = False
    call screen level_clear(9, 3, l9_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch9_B:
    scene bg_living
    mc confused "我是个小学生，怎么可能洗钱？到底是什么案子？"
    l9_cop serious "你的身份信息被犯罪团伙冒用，开通的电话卡发送了大量诈骗短信！现在有两条路：一是配合资金清查自证清白，二是明天由当地民警上门逮捕你！"
    n "紧接着，「李警官」发来一张带照片的「刑事拘捕令」，阿狐的名字和照片赫然在列，还盖着鲜红的大印。"
    l9_cop serious "此案属于机密！不准告诉任何人，包括你父母，否则以泄密罪论处！现在开始视频做笔录，全程不许挂断！"

    menu:
        "违反「保密要求」，把事情告诉妈妈":
            jump ch9_B1
        "不信「通缉令」，拒绝配合并挂断电话":
            jump ch9_B2
        "被「通缉令」吓住，配合视频做笔录":
            jump ch9_B3


# B1：违反保密告诉妈妈 · 满分
label ch9_B1:
    scene bg_living
    n "阿狐越听越害怕，但「不准告诉父母」这句话反而让他起了疑心。"
    think worried "让我瞒着爸妈的「警察」，为什么这么怕大人知道？不对劲！"
    n "阿狐没有挂断电话，借口写作业，偷偷给妈妈发了消息。妈妈立刻打来电话，让他什么都不用做，马上拨打96110。"
    mom serious "宝贝，这是「冒充公检法」诈骗！通缉令是P的图，公安机关办案从不保密到不许告诉家人，更不会电话办案！"
    n "妈妈陪阿狐拉黑号码、开启拦截，还拨打了96110备案。"

    scene bg_bedroom
    police laugh "关键一步走对了！凡是让你「保密」「不许告诉家人」的「警察」，百分之百是骗子！反诈专线96110，随时帮您核实！"

    $ clear_chapter(9, 3)
    $ quick_menu = False
    call screen level_clear(9, 3, l9_tip)
    $ quick_menu = True
    jump select_level


# B2：识破通缉令 · 及时止损（2星）
label ch9_B2:
    scene bg_living
    n "阿狐盯着那张「通缉令」看了半天，忽然发现不对劲。"
    think serious "真通缉令怎么会用手机发过来？照片还是我班级群里的头像！老师说过，公检法办案都是当面出示证件！"
    mc serious "我不配合。真警察不会电话办案，更不会用微信发通缉令，你是骗子！"
    n "阿狐挂断电话并拉黑号码。对方又换了两个号码打来，都被拦截了。"
    n "晚上妈妈回家，阿狐说明了情况，妈妈立刻拨打了96110备案，并开启了全家骚扰拦截。"

    scene bg_living
    police serious "识破PS通缉令，干得漂亮！记住三个「绝不会」：公检法绝不会电话办案、绝不会发「安全账户」、绝不会让你瞒着家人。"

    $ clear_chapter(9, 2)
    $ quick_menu = False
    call screen level_clear(9, 2, l9_tip)
    $ quick_menu = True
    jump select_level


# B3：配合做笔录 · 轻微泄露（1星）
label ch9_B3:
    scene bg_living
    n "看着盖着红章的「通缉令」，阿狐吓坏了，按对方要求开始了「视频笔录」。"
    n "对方逐一询问了家庭住址、爸爸妈妈的工作单位、银行卡信息，还让他下载了一个「办案协作APP」开启屏幕共享。"
    n "视频里，「李警官」突然要求：把妈妈手机收到的银行验证码报给他，「清查资金流水，证明清白」。"
    n "就在这时，妈妈提前下班回了家，一把抢过手机挂断了视频。"
    mom serious "这是诈骗！验证码差点就被骗走，银行卡里的钱就危险了！"
    n "妈妈立刻修改了银行密码、解绑快捷支付，并拨打了96110备案。"

    scene bg_bedroom
    police serious "好险！个人信息、银行卡号已经泄露，好在验证码没给出去。「屏幕共享」等于把银行卡摊在骗子眼皮底下，一个验证码都发不得！"

    $ clear_chapter(9, 1)
    $ quick_menu = False
    call screen level_clear(9, 1, l9_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch9_C:
    scene bg_living
    n "阿狐不敢怠慢，把家庭情况一一交代了。"
    think worried "警察叔叔的问题我都老实回答了，应该很快就能证明清白吧……"
    l9_cop serious "初步查明，你妈妈银行卡里的资金有问题！为了证明清白，需要把存款转入「安全账户」进行资金公证，查完原路退还！"
    l9_cop serious "马上下载「资金清查APP」，打开屏幕共享，我一步步教你操作！记住，此案高度保密，不许告诉任何人！"

    menu:
        "输入密码前猛然醒悟，挂断电话":
            jump ch9_C1
        "心存侥幸，只报银行卡号试试":
            jump ch9_C2
        "照做：屏幕共享，配合资金清查":
            jump ch9_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch9_C1:
    scene bg_living
    n "手指即将点下下载按钮，阿狐心里突然咯噔一下。"
    think serious "等等！老师说过，根本没有「安全账户」，公检法办案也不会视频指导转账！越是不让告诉家人的，越是骗子！"
    mc serious "我不下载！真警察有意见请上门找我爸爸，或者我们打96110核实，你敢报真名吗？"
    n "电话那头瞬间哑口无言，随即挂断。阿狐马上给妈妈打电话，妈妈拨打了96110备案并开启拦截。"

    scene bg_bedroom
    police serious "反应出色！「安全账户」是冒充公检法骗局的核心话术——记住：让你转账的「警察」都是骗子，96110才是真正的反诈热线！"

    $ clear_chapter(9, 3)
    $ quick_menu = False
    call screen level_clear(9, 3, l9_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微泄露（1星）
label ch9_C2:
    scene bg_living
    n "阿狐既怕被「逮捕」，又不敢下载奇怪的APP，决定先报银行卡号「配合一下」。"
    think laugh "只给卡号，不给密码不给验证码，应该出不了事吧。"
    n "卡号报过去，「李警官」却步步紧逼：流水显示异常，需提供短信验证码完成「资金公证」，否则今晚就上门拘捕。"
    mc confused "怎么问完卡号又要验证码？越问越深了……"
    n "阿狐慌忙挂断电话找妈妈。妈妈立刻挂失补办银行卡、修改所有支付密码。"
    n "所幸验证码没有泄露，卡里的钱保住了，但办卡、换卡折腾了整整一周。"

    scene bg_living
    police serious "卡号、身份证号都会被骗子利用！面对冒充公检法，正确的动作只有一个：挂断电话，拨打96110，告诉家人。侥幸心理要不得！"

    $ clear_chapter(9, 1)
    $ quick_menu = False
    call screen level_clear(9, 1, l9_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch9_C3:
    scene bg_living
    n "阿狐被「今晚拘捕」吓坏了，乖乖下载了「资金清查APP」，打开屏幕共享。"
    n "屏幕共享状态下，「李警官」一步步指挥他：输入妈妈手机的支付密码、读出刚收到的验证码、确认「资金公证」转账。"
    n "几分钟后，妈妈卡里的48000元被分三笔转走。电话挂断，「李警官」再也联系不上。"
    mc sad "妈妈……妈妈的钱被我在电话里转走了……我该怎么办……"
    n "妈妈回家后，阿狐哭着说明了经过。妈妈没有责骂他，立刻报警并联系银行冻结账户，但大部分钱已被转走。"
    mom normal "不怪你，是骗子太狡猾。记住：以后凡是电话里谈到钱和密码的，一律挂断，等妈妈回来。"

    scene bg_bedroom
    police serious "小朋友记住！「冒充公检法」是损失最惨重的骗局：假警官、假通缉令、假安全账户，最后用屏幕共享掏空你的银行卡。真警察从不电话办案，96110永远为你核实！"

    $ quick_menu = False
    call screen level_fail(9, l9_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch9
    else:
        jump select_level
