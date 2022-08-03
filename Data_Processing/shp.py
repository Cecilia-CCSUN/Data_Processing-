# shp相交计算
import os
import pandas as pd
from osgeo import gdal, ogr
import sys

from osgeo.gdalconst import GA_ReadOnly

driver = ogr.GetDriverByName('ESRI Shapefile')
shp1 = r"D:\研一\数据\IhChina_2006-2021\test.shp"
shp2 = r"D:\研一\数据\生态文明模式数据\Origin_Data.shp"
ds1 = driver.Open(shp1, 0)
ds2 = driver.Open(shp2, 0)
if ds2 is None:
    print('打开矢量文件失败')
    sys.exit(1)
else:
    print('打开矢量文件成功')


layer1 = ds1.GetLayer(0)
layer2 = ds2.GetLayer(0)


'''循环遍历所有的该图层中所有的要素'''
 #复位

# print(layer1.GetFeatureCount())
# print(layer2.GetFeatureCount())

xValues1 = []
yValues1 = []
for i in range(layer1.GetFeatureCount()):
    feature = layer1.GetFeature(i)
    geometry = feature.GetGeometryRef()
    x1 = geometry.GetX()
    y1 = geometry.GetY()
    xValues1.append(x1)
    yValues1.append(y1)
    # print(x1,y1)

    for j in range(layer2.GetFeatureCount()):
        # extent = layer2.GetExtent()
        # print('extent:', extent)
        # print('ul:', extent[0], extent[1])  # 左右边界
        # print('lr:', extent[2], extent[3])  # 下上边界
        n = layer2.GetFeatureCount()  # 该图层中有多少个要素
        feat = layer2.GetFeature(j)  # 提取数据层中的第一个要素
        geom = feat.GetGeometryRef()  # 提取该要素的轮廓坐标
        name = feat.GetField('县名')  # 读取该要素字段名为'FieldID'的值，注意读取'shape'字段会报错


        pt = ogr.Geometry(ogr.wkbPoint)
        pt.AddPoint(x1, y1)
        # print(type(pt))
        if pt.Within(geom):
            print(name)
            break
    if pt.Within(geom)== False:
        print(-1)











