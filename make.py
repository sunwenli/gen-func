#coding=utf-8
import os
import time
import datetime
from random import Random

tps_val = [('void', ''),
           ('BOOL ', 'YES'),
           ('NSString *', '@"string"'),
           ('int ', '123'),
           ('NSArray *', '[NSArray array]'),
           ('NSMutableArray *', '[NSMutableArray arrayWithCapacity:1]'),
           ('NSDictionary *', '[NSDictionary dictionary]'),
           ('NSMutableDictionary *', '[NSMutableDictionary dictionaryWithCapacity:1]')]

inherited_cls = ['NSObject', 'UIViewController', 'UIView']

tps_params_fir = [('int', 'it'),
                  ('BOOL', 'bl'),
                  ('NSString *', 'str'),
                  ('NSArray *', 'arr'),
                  ('NSMutableArray *', 'mutArr'),
                  ('NSDictionary *', 'dict'),
                  ('NSMutableDictionary *', 'mutDict')]
tps_params_next = [('int', 'withIt', 'withInt'), ('BOOL', 'withBl', 'withBOOL'), ('NSString *', 'withStr', 'withStr'),
                   ('NSDictionary *', 'withDict', 'withDict'), ('NSMutableDictionary *', 'withMutDict', 'withMutDict'),
                   ('NSArray *', 'withArr', 'withArray'), ('NSMutableArray *', 'withMutArr', 'withMutArray')]


def make_code(des_path, fun_num, class_name, target_name):
    print 'make_ios_code'
    new_class_h_path = des_path + '/' + class_name + '.h'
    print new_class_h_path
    if not os.path.exists(des_path):
        os.makedirs(des_path)
    new_class_m_path = des_path + '/' + class_name + '.m'
    print new_class_m_path
    print_format_h(new_class_h_path, class_name, target_name)

    new_class_m_path2 = des_path + '/' + class_name + '2.m'
    new_class_m_path3 = des_path + '/' + class_name + '3.m'

    out2 = open(new_class_m_path2, 'w')
    out2.write('//\n')
    out2.write('//\t'+class_name+'.m\n')
    out2.write('//\t'+target_name+'\n')
    out2.write('//\n')
    out2.write('//\t'+'Created by SUN on '+time.strftime("%Y/%m/%d", time.localtime())+'.'+'\n')
    out2.write('//\t'+'Copyright © '+str(datetime.datetime.now().year)+' SUN. All rights reserved.'+'\n')
    out2.write('//\n\n')
    out2.write('#import "'+class_name+'.h"'+'\n\n')
    out2.write('@implementation '+class_name+'\n\n')
    out2.write('static '+class_name+' *mode'+class_name+' = nil;\n')
    out2.write('+ ('+class_name+' *)share'+class_name+' {\n')
    out2.write('\tif (!mode'+class_name+') {\n')
    out2.write('\t\t[mode'+class_name+' = [['+class_name+' alloc] init];\n')

    out3 = open(new_class_m_path3, 'w')
    print_format_m(new_class_m_path, new_class_m_path2, new_class_m_path3, out2, out3, class_name, 0, fun_num)
    out2 = open(new_class_m_path, 'a+')
    out2.write('@end\n')
    out2.close()


def print_format_h(file_path, cls_name, target_name):
    print 'print_format_h'
    out = open(file_path, 'w')
    out.write('//\n')
    out.write('//\t'+cls_name+'.h\n')
    out.write('//\t'+target_name+'\n')
    out.write('//\n')
    out.write('//\t'+'Created by SUN on '+time.strftime("%Y/%m/%d", time.localtime())+'.'+'\n')
    out.write('//\t'+'Copyright © '+str(datetime.datetime.now().year)+' SUN. All rights reserved.'+'\n')
    out.write('//\n\n')
    out.write('#import <UIKit/UIKit.h>\n\n')
    inherited_cls_idx = Random().randint(0, 2)
    out.write('@interface '+cls_name+' : '+inherited_cls[inherited_cls_idx]+'\n\n')
    out.write('+ ('+cls_name+' *)share'+cls_name+';\n\n')
    out.write('@end\n')
    out.close()


def print_format_m(new_cls_m_path, new_cls_m_path2, new_cls_m_path3, out2, out3, cls_name, idx, fun_num):
    print 'print_format_m'
    while idx < int(fun_num):
        print idx
        tp_val_idx = Random().randint(0, 6)
        tp = tps_val[tp_val_idx][0]
        val = tps_val[tp_val_idx][1]
        n_fun_name = random_str(8)
        fun_name_param = gen_fun_name(n_fun_name)
        if n_fun_name == fun_name_param:
            out2.write('\t\t[mode'+cls_name+' '+n_fun_name+'];\n')
        out3.write('- ('+tp+')'+fun_name_param+' {\n')
        ret_val = random_str(5)
        out3.write('\tNSLog(@"运行到 '+n_fun_name+'");\n')
        if tp != 'void':
            out3.write('\t'+tp+ret_val+' = '+val+';\n')
            out3.write('\treturn '+ret_val+';\n')
        out3.write('}\n\n')
        idx += 1
    out2.write('\t}\n')
    out2.write('\treturn mode'+cls_name+';\n')
    out2.write('}\n\n')

    out2.close()
    out3.close()

    out2 = open(new_cls_m_path2, 'r+')
    content2 = out2.read()
    out3 = open(new_cls_m_path3, 'r+')
    content3 = out3.read()

    f = open(new_cls_m_path, "w")
    f.write(content2+'\n'+content3)
    f.close()
    os.remove(new_cls_m_path2)
    os.remove(new_cls_m_path3)


def gen_fun_name(n_fun_name):
    param_num = Random().randint(0, 3)
    if param_num == 0:
        return n_fun_name
    elif param_num > 0:
        tmp_name = ''
        dump_idx = Random().randint(0, 6)
        for i in range(param_num):
            idx = Random().randint(0, 6)
            if i == 0:
                tmp_name = n_fun_name + ':('+tps_params_fir[idx][0]+')'+tps_params_fir[idx][1]
            else:
                while idx == dump_idx:
                    idx = Random().randint(0, 6)
                dump_idx = idx
                tmp_name += ' '+tps_params_next[idx][2]+':('+tps_params_next[idx][0]+')'+tps_params_next[idx][1]
        return tmp_name


def random_str(random_len=8):
    random_s = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(chars) - 1
    random = Random()
    for i in range(random_len):
        random_s += chars[random.randint(0, length)]
    return random_s
