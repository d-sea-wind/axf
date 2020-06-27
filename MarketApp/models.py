#coding=utf-8
from django.db import models

# Create your models here.

# insert into axf_foodtype(typeid,typename,childtypenames,typesort)
# values("104749","热销榜","全部分类:0",1),("104747","新品尝鲜","全部分类:0",2),("103532","优选水果","全部分类:0#进口水果:103534#国产水果:103533",3),("103581","卤味熟食","全部分类:0",4),("103536","牛奶面包","全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540",5),("103549","饮料酒水","全部分类:0#饮用水:103550#茶饮/咖啡:103554#功能饮料:103553#酒类:103555#果汁饮料:103551#碳酸饮料:103552#整箱购:104503#植物蛋白:104489#进口饮料:103556",6),("103541","休闲零食","全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545",7),("103557","方便速食","全部分类:0#方便面:103558#火腿肠卤蛋:103559#速冻面点:103562#下饭小菜:103560#罐头食品:103561#冲调饮品:103563",8),("103569","粮油调味","全部分类:0#杂粮米面油:103570#厨房调味:103571#调味酱:103572",9),("103575","生活用品","全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577",10),("104958","冰激凌","全部分类:0",11);
# foodtype
class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()
    class Meta:
        db_table = 'axf_foodtype'

# INSERT INTO axf_goods
# (id, productid, productimg, productname, productlongname,
# isxf, pmdesc, specifics, price, marketprice,
# categoryid, childcid, childcidname, dealerid, storenums, productnum)
# VALUES (1, 11951, '/media/images/goods016.jpg', '', '乐吧薯片鲜虾味50.0g',
# 0, 0, '50g', 2, 2.5,
# 103541, 103543, '膨化食品', 4858, 200, 4);
class AxfGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=256)
    productname = models.CharField(max_length=256)
    productlongname = models.CharField(max_length=256)
    isxf = models.BooleanField()
    pmdesc = models.BooleanField()
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=128)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = 'axf_goods'


