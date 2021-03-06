# 公共错误码（30000-31000）
# v3API将使用统一30000开头的错误码
# 公共错误码包括签名以及各个业务线统一的错误码

ERRORCODE = {}
ERRORCODE['30001'] = u'请求头"OK_ACCESS_KEY"不能为空'
ERRORCODE['30002'] = u'请求头"OK_ACCESS_SIGN"不能为空'
ERRORCODE['30003'] = u'请求头"OK_ACCESS_TIMESTAMP"不能为空'
ERRORCODE['30004'] = u'请求头"OK_ACCESS_PASSPHRASE"不能为空'
ERRORCODE['30005'] = u'无效的OK_ACCESS_TIMESTAMP'
ERRORCODE['30006'] = u'无效的OK_ACCESS_KEY'
ERRORCODE['30007'] = u'无效的Content_Type，请使用“application/json”格式'
ERRORCODE['30008'] = u'请求时间戳过期'
ERRORCODE['30009'] = u'系统错误'
ERRORCODE['30010'] = u'api 校验失败'
ERRORCODE['30011'] = u'无效的ip'
ERRORCODE['30012'] = u'无效的授权'
ERRORCODE['30013'] = u'无效的sign'
ERRORCODE['30014'] = u'请求太频繁'
ERRORCODE['30015'] = u'请求头"OK_ACCESS_PASSPHRASE"错误'
ERRORCODE['30016'] = u'您使用的是v1的apiKey，请调用v1接口。若您希望调用v3接口，请注册v3的apiKey'
ERRORCODE['30017'] = u'apikey所属broker ID不匹配'
ERRORCODE['30018'] = u'apikey所属域名不匹配'
ERRORCODE['30019'] = u'OKEX Null Code'

ERRORCODE['30020'] = u'Post 请求body不能为空'
ERRORCODE['30021'] = u'json数据格式错误'
ERRORCODE['30022'] = u'OKEX Null Code'
ERRORCODE['30023'] = u'必填参数不能为空'
ERRORCODE['30024'] = u'参数值填写错误'
ERRORCODE['30025'] = u'参数类型错误'
ERRORCODE['30026'] = u'用户请求频率过快，超过该接口允许的限额'
ERRORCODE['30027'] = u'登录失败'
ERRORCODE['30028'] = u'非本人操作'
ERRORCODE['30029'] = u'用户被冻结'
ERRORCODE['30030'] = u'请求接口失败，请您重试'
ERRORCODE['30031'] = u'请求的币种不存在'
ERRORCODE['30032'] = u'请求的币对不存在'
ERRORCODE['30033'] = u'验证apikey所属交易所，为空'
ERRORCODE['30034'] = u'验证apikey所属交易所ID，为空'
ERRORCODE['30035'] = u'该交易已关闭'
ERRORCODE['30036'] = u'没有相应数据'
ERRORCODE['30037'] = u'接口已下线或无法使用'
ERRORCODE['30038'] = u'用户不存在'

# 交割合约错误码（32000-33000）
ERRORCODE['32001'] = u'合约账户被冻结'
ERRORCODE['32002'] = u'用户合约账户不存在'
ERRORCODE['32003'] = u'撤单中，请耐心等待'
ERRORCODE['32004'] = u'您当前没有未成交的订单'
ERRORCODE['32005'] = u'超过最大下单量'
ERRORCODE['32006'] = u'委托价格或触发价格超过100万美元'
ERRORCODE['32007'] = u'合约相同方向只支持一个杠杆'
ERRORCODE['32008'] = u'(全仓)的时候大于最多可开仓位'
ERRORCODE['32009'] = u'(逐仓)的时候大于最多可开仓位'
ERRORCODE['32010'] = u'当前有持仓，无法设置杠杆'
ERRORCODE['32011'] = u'使用了过期的合约'
ERRORCODE['32012'] = u'撤单完订单状态更新'
ERRORCODE['32013'] = u'币种类型为空'
ERRORCODE['32014'] = u'平仓张数大于该仓位的可平张数'
ERRORCODE['32015'] = u'开仓前保证金率低于100%'
ERRORCODE['32016'] = u'开仓后保证金率低于100%'
ERRORCODE['32017'] = u'暂无对手价'
ERRORCODE['32018'] = u'下单数量不足1张，请重新选择'
ERRORCODE['32019'] = u'开多的时候超过103% 开低的时候低于97%'
ERRORCODE['32020'] = u'价格不在限价范围内'
ERRORCODE['32021'] = u'设置杆杆的时候不是设置的10倍或者20倍'
ERRORCODE['32022'] = u'根据相关法律，您所在的国家或地区不能使用该功能'
ERRORCODE['32023'] = u'账户存在借款'
ERRORCODE['32024'] = u'合约交割中，无法下单'
ERRORCODE['32025'] = u'合约清算中，无法下单'
ERRORCODE['32026'] = u'您的账户已被限制开仓操作'
ERRORCODE['32027'] = u'撤单的时候数量超过限制'
ERRORCODE['32028'] = u'用户爆仓冻结'
ERRORCODE['32029'] = u'重复撤单，订单信息不存在'


# 币币和杠杆错误码（33000-34000）
ERRORCODE['33001'] = u'您尚未开通此币种对应杠杆业务'
ERRORCODE['33002'] = u'您的此币种对应杠杆账号已被冻结'
ERRORCODE['33003'] = u'没有足够的余额进行借币'
ERRORCODE['33004'] = u'借币数量不能小于最小借币数'
ERRORCODE['33005'] = u'还款金额不能小于等于0'
ERRORCODE['33006'] = u'没有该借币订单'
ERRORCODE['33007'] = u'不存在该状态'
ERRORCODE['33008'] = u'借币数量不能大于您的可借数量'
ERRORCODE['33009'] = u'集合竞价时候不可以撤单'
ERRORCODE['33010'] = u'当前有持仓，无法设置杠杆'
ERRORCODE['33011'] = u'没有最新行情信息'
ERRORCODE['33012'] = u'撤单失败'
ERRORCODE['33013'] = u'下单失败'
ERRORCODE['33014'] = u'重复撤单，订单不存在'
ERRORCODE['33015'] = u'批量操作超过最大数量限制'
ERRORCODE['33016'] = u'该币对没有开通杠杆业务'
ERRORCODE['33017'] = u'下单大于最大可用余额'
ERRORCODE['33018'] = u'获取深度接口时参数不对'
ERRORCODE['33019'] = u'OKEX Null'
ERRORCODE['33020'] = u'有些交易所不支持杠杆业务'
ERRORCODE['33021'] = u'还币时币与币对不匹配'
ERRORCODE['33022'] = u'还币时币与订单不匹配'
ERRORCODE['33023'] = u'集合竞价时只可以下市价单'
ERRORCODE['33024'] = u'交易金额小于最小交易值'
ERRORCODE['33025'] = u'下单时上币时候币对配置不全'
ERRORCODE['33026'] = u'撤单时完成交易的订单不能撤单'
ERRORCODE['33027'] = u'撤单时已经撤销和撤销中的订单不能撤单'
ERRORCODE['33028'] = u'交易价格小数位数超过限制'
ERRORCODE['33029'] = u'交易数量小数位数超过限制'

# 钱包错误码（34000-35000）
ERRORCODE['34001'] = u'提现接口，账户被冻结'
ERRORCODE['34002'] = u'提现接口，地址未添加'
ERRORCODE['34003'] = u'该币种暂不支持提现至该地址'
ERRORCODE['34004'] = u'提现手续费小于最小值'
ERRORCODE['34005'] = u'提现手续费大于最大值'
ERRORCODE['34006'] = u'提现金额小于最小提现金额'
ERRORCODE['34007'] = u'提现金额大于单笔提现最大金额'
ERRORCODE['34008'] = u'划转和提现接口，余额不足'
ERRORCODE['34009'] = u'今日提现金额累计超过每日限额'
ERRORCODE['34010'] = u'转账金额必须大于零'
ERRORCODE['34011'] = u'划转提现接口，不符合条件，如kyc等级不够'
ERRORCODE['34012'] = u'提现接口，某些币特殊限制'
ERRORCODE['34013'] = u'划转接口，转入或转出是币币杠杆时instrument ID未传'
ERRORCODE['34014'] = u'划转接口，划转资金受限'
ERRORCODE['34015'] = u'子账户不存在'
ERRORCODE['34016'] = u'划转接口，源或目的不允许划转'
ERRORCODE['34017'] = u'划转接口，账户冻结'
ERRORCODE['34018'] = u'交易密码错误'
ERRORCODE['34019'] = u'您需要绑定邮箱后，才能提现'
ERRORCODE['34020'] = u'您需设置资金密码后，才能提现'
ERRORCODE['34021'] = u'提现接口，不是认证的地址'
ERRORCODE['34022'] = u'提现接口，子账号不允许提现'