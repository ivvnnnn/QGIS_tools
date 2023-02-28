interactive_mode  = 0

layers = ['line', 'poly']
line_layer_name = layers[0]
poly_layer_name = layers[1]
line_layer = QgsProject.instance().mapLayersByName(line_layer_name)
poly_layer = QgsProject.instance().mapLayersByName(poly_layer_name)
buffer_size = 1.3
ecs = QgsGeometry.EndCapStyle(QgsGeometry.CapFlat)
js =  QgsGeometry.JoinStyle(QgsGeometry.JoinStyleMiter)

segments_num = 7


interactive_mode = 0
'''
def create_buffer():
    features = line_layer[0].getFeatures()
    for feat in features:
        last_ = feat
    line_geom = last_.geometry()
    buffer_ = line_geom.buffer(10,0, ecs,js,0.9)
    
    poly_feat =  poly_layer[0].getFeature(0)
    #poly_feat.setGeometry(buffer_)

    print ('ID:', poly_feat.id())
    fet = QgsFeature()
    fet.setGeometry(buffer_)
    dp = poly_layer[0].dataProvider()
    dp.addFeatures([fet])
    print(dp)
    
'''



selected_features = line_layer[0].selectedFeatures()
print(selected_features)


try:
    for line_feat in selected_features:
        line_geom = line_feat.geometry()
        buffer_ = line_geom.buffer(buffer_size,segments_num, ecs,js,0.9)
        #print('Buffer:', buffer_)
        poly_feat =  poly_layer[0].getFeature(0)
        print ('ID:', poly_feat.id())
        
    
        fet = QgsFeature()
        fet.setGeometry(buffer_)
        dp = poly_layer[0].dataProvider()
        dp.addFeatures([fet])
        print('DP:', dp)
except:
    print('Выделен объект не в слое', layers[0])
    
    #poly_feat =  poly_layer[0].getFeature(0)
    #poly_feat.setGeometry(buffer_)




