# -*- coding: utf-8 -*-

import core
core.face_merge(src_img=template_file_path,
                dst_img=dst_image_file_path,
                out_img=out_img_path,
                alpha=0.8,
                blur_detail_x=15,
                blur_detail_y=10,
                mat_multiple=0.9,
                correct_color_enable=1)
            