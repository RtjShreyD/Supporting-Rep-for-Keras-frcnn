import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['Image_names', '', '', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def filter():
        path = os.path.join(os.getcwd(), 'data', 'test_labels.csv')
        f1=pd.read_csv(path)
        keep_col = ['Image_names','cell_type', 'xmin', 'xmax', 'ymin', 'ymax']
        new_f1 = f1[keep_col]
        new_f1.to_csv("test.csv", index=False)
        print('filter success on test')

        path2 = os.path.join(os.getcwd(), 'data', 'train_labels.csv')
        f2=pd.read_csv(path2)
        keep_col = ['Image_names','cell_type', 'xmin', 'xmax', 'ymin', 'ymax']
        new_f2 = f2[keep_col]
        new_f2.to_csv("train.csv", index=False)
        print('filter success on train')

def main():
    for directory in ['train','test']:
        image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')
        filter()

main()
