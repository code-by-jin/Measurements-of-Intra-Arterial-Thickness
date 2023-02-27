def plot_artery_ann(vis, cnt_outer, cnts_mid, cnts_inner):
    cv2.drawContours(vis, [cnt_outer], -1, [255, 0, 0], 2)
    cv2.drawContours(vis, cnts_mid, -1, [0, 255, 0], 2)
    cv2.drawContours(vis, cnts_inner, -1, [0, 0, 255], 2)
    return vis

def save_img(img, wsi_id, artery_id):
    dir_save_wsi = os.path.join(DIR_SAVE_FIGURE, wsi_id)
    if not os.path.exists(dir_save_wsi):
        os.makedirs(dir_save_wsi)
    path_to_svae = os.path.join(dir_save_wsi, artery_id+'.png')
    Image.fromarray(img).save(path_to_svae)
    
def imshow_two_in_row(arr_0, arr_1): 
    plt.figure(figsize=(10, 10))    
    plt.subplot(1, 2, 1)
    plt.imshow(arr_0, cmap=plt.cm.gray, vmin=0, vmax=255)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(arr_1, cmap=plt.cm.gray, vmin=0, vmax=255)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
def save_img_helper(img, wsi_id, artery_id, sample_id):
            
    dir_save_wsi = os.path.join(DIR_SAVE_FIGURE, wsi_id, artery_id)
    if not os.path.exists(dir_save_wsi):
        os.makedirs(dir_save_wsi)
    if sample_id >= 10:
        sample_id_str = str(sample_id)
    else:
        sample_id_str = "0" + str(sample_id)
    path_to_svae = os.path.join(dir_save_wsi, sample_id_str+'.png')
    Image.fromarray(img).save(path_to_svae)