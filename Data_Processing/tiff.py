# 获取栅格值
import os
import pandas as pd
from osgeo import gdal, ogr
import sys

from osgeo.gdalconst import GA_ReadOnly

value = 0.
driver = ogr.GetDriverByName('ESRI Shapefile')
shp = "D:\\研一\\数据\\textdata\\6.shp"
ds = driver.Open(shp, 0)
# if ds is None:
#     print('打开矢量文件失败')
#     sys.exit(1)
# else:
#     print('打开矢量文件成功')

layer = ds.GetLayer(0)
# print(layer.GetFeatureCount())
xValues = []
yValues = []
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    geometry = feature.GetGeometryRef()
    x = geometry.GetX()
    y = geometry.GetY()
    xValues.append(x)
    yValues.append(y)
    # print(x,y)

    # 开始对栅格的操作
    # GDAL所有操作都需要先注册格式
    # 一次性注册所有的数据驱动，但是只能读不能写：gdal.AllRegister()
gdal.AllRegister()
    # 打开数据集，并传递数据集的名称和所需的访问权限（GA_ReadOnly或GA_Update）
img = "D:\\研一\\数据\\China_DEM\\1km\\Extract_DEM_China1.tif"
dr = gdal.Open(img, GA_ReadOnly)
# if dr is None:
#     print('打开栅格文件失败')
#     sys.exit(1)
# else:
#     print("打开栅格后的数据")
# 读取图像y方向上的像素个数
rows = dr.RasterYSize
# print(rows)
    # 读取图像x方向上的像素个数
cols = dr.RasterXSize
# print(cols)
    # 波段数
bands = dr.RasterCount


    #存储着栅格数据集的地理坐标信息
transform = dr.GetGeoTransform()
    #影像左上角横坐标
xOrigin = transform[0]
    #影像左上角纵坐标
yOrigin = transform[3]
    #遥感图像的水平空间分辨率或者东西方向上的像素分辨率
pixelWidth = transform[1]
    #遥感图像的垂直空间分辨率或者南北方向上的像素分辨率
pixelHeight = transform[5]
    #通常geoTransform[5] 与 geoTransform[1]相等


values = []
    #循环遍历矢量坐标
j=0
for i in range(len(xValues)):
    x = xValues[i]
    y = yValues[i]

        #计算某一坐标对应像素的相对位置(pixel offset)，也就是该坐标与左上角的像素的相对位置，按像素数计算
    xOffset = int((x - xOrigin) / pixelWidth)
    yOffset = int((y - yOrigin) / pixelHeight)
    # print(xOffset,yOffset)
    if xOffset < 0 or xOffset > cols or yOffset < 0 or yOffset > rows:
        value = -1
        print(value)

    # if xOffset+1 < 0 or xOffset+1 > cols or yOffset < 0 or yOffset > rows:
    #     value = -1
    #     print(value)
    # if xOffset-1 < 0 or xOffset-1 > cols or yOffset < 0 or yOffset > rows:
    #     value = -1
    #     print(value)
    # if xOffset-1 < 0 or xOffset-1 > cols or yOffset < 0 or yOffset > rows:
    #     value = -1
    #     print(value)
    # if xOffset < 0 or xOffset > cols or yOffset+1 < 0 or yOffset+1 > rows:
    #     value = -1
    #     print(value)
    # if xOffset < 0 or xOffset > cols or yOffset-1 < 0 or yOffset-1 > rows:
    #     value = -1
    #     print(value)
    # if xOffset-1 < 0 or xOffset-1 > cols or yOffset - 1 < 0 or yOffset - 1 > rows:
    #     value = -1
    #     print(value)
    # if xOffset-1 < 0 or xOffset-1 > cols or yOffset+1 < 0 or yOffset+ 1 > rows:
    #     value = -1
    #     print(value)
    # if xOffset+1 < 0 or xOffset+1 > cols or yOffset-1 < 0 or yOffset- 1 > rows:
    #     value = -1
    #     print(value)
    # if xOffset+1 < 0 or xOffset+1 > cols or yOffset+1 < 0 or yOffset+ 1 > rows:
    #     value = -1
    #     print(value)
    # s = str(int(x)) + ' ' + str(int(y)) + ' ' + str(xOffset) + ' ' + str(yOffset) + ' '
    # print(s)
    else :
        d1 = dr.ReadAsArray(xOffset, yOffset, 1, 1)
        d2 = dr.ReadAsArray(xOffset+1, yOffset, 1, 1)
        d3 = dr.ReadAsArray(xOffset-1, yOffset, 1, 1)
        d4 = dr.ReadAsArray(xOffset, yOffset+1, 1, 1)
        d5 = dr.ReadAsArray(xOffset, yOffset-1 ,1, 1)
        d6 = dr.ReadAsArray(xOffset-1,yOffset+1,1,1)
        d7 = dr.ReadAsArray(xOffset-1,yOffset-1,1,1)
        d8 = dr.ReadAsArray(xOffset+1,yOffset-1,1,1)
        d9 = dr.ReadAsArray(xOffset+1,yOffset+1,1,1)


    #     #创建一个要打印的字符串
    #     #s = str(int(x)) + ' ' + str(int(y)) + ' ' + str(xOffset) + ' ' + str(yOffset) + ' '
    #     #print("矢量点：x值 y值 x偏移量 y偏移量"+s)
    #
    #     # 把图像中位于xOffset，xOffset，宽度为1高度为1的数据读取出来了
    #     # 此处将矢量对应的栅格值读取出来
    #     # row对应y轴，col对应x轴。

        value1 = d1[0,0]
        value2 = d2[0,0]
        value3 = d3[0,0]
        value4 = d4[0,0]
        value5 = d5[0, 0]
        value6 = d6[0, 0]
        value7 = d7[0, 0]
        value8 = d8[0, 0]
        value9 = d9[0, 0]
        if value1 > 6340 or value1 < -124:
            value = 0

        if value2 > 6340 or value2 < -124:
            value2 = 0

        if value3 > 6340 or value3 < -124:
            value3 = 0

        if value4 > 6340 or value4 < -124:
            value4 = 0

        if value5 > 6340 or value5 < -124:
            value5 = 0

        if value6 > 6340 or value6 < -124:
            value6 = 0
        if value7 > 6340 or value7 < -124:
            value7 = 0
        if value8 > 6340 or value8 < -124:
            value8 = 0
        if value9 > 6340 or value9 < -124:
            value9 = 0



        value = value1*0.6 + (value2+value3+value4+value5) * 0.3/4 + (value6+value7+value8+value9)*0.2/4
        print(value)

