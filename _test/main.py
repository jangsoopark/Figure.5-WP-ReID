from rcpm.dataset import DataBank
from rcpm.eval import update_with_gps
from pathlib import Path
from rcpm.utils import DataPacker, file_abs_path

if __name__ == '__main__':
    wp_reid_dataset = DataBank(
        minframes=3,
        raw_data_folder=Path('/data'),
        cropped_image_dir=Path('/data') / 'cropped_data',
        split_file_dir=file_abs_path(__file__) / 'files/wp_reid_info.json'
    )

    files_dir = file_abs_path(__file__) / 'files'
    mmt_duke_dist_file = files_dir / 'mmt_duke_g2g_distmat.json'
    mmt_mars_dist_file = files_dir / 'mmt_mars_g2g_distmat.json'
    ssg_duke_dist_file = files_dir / 'ssg_duke_g2g_distmat.json'
    ssg_mars_dist_file = files_dir / 'ssg_mars_g2g_distmat.json'
    tkp_duke_dist_file = files_dir / 'tkp_duke_g2g_distmat.json'
    tkp_mars_dist_file = files_dir / 'tkp_mars_g2g_distmat.json'

    print('MMT Duke')
    distmat = DataPacker.load(mmt_duke_dist_file)['g2g_distmat']
    update_with_gps(distmat, wp_reid_dataset.test_info, wp_reid_dataset.probe_index, wp_reid_dataset.gallery_index,
                    wp_reid_dataset.gps_info, wp_reid_dataset.trajectory_info, k=8)

    print('MMT MARS')
    distmat = DataPacker.load(mmt_mars_dist_file)['g2g_distmat']
    update_with_gps(distmat, wp_reid_dataset.test_info, wp_reid_dataset.probe_index, wp_reid_dataset.gallery_index,
                    wp_reid_dataset.gps_info, wp_reid_dataset.trajectory_info, k=9)

    print('SSG Duke')
    distmat = DataPacker.load(ssg_duke_dist_file)['g2g_distmat']
    update_with_gps(distmat, wp_reid_dataset.test_info, wp_reid_dataset.probe_index, wp_reid_dataset.gallery_index,
                    wp_reid_dataset.gps_info, wp_reid_dataset.trajectory_info, k=4)

    print('SSG MARS')
    distmat = DataPacker.load(ssg_mars_dist_file)['g2g_distmat']
    update_with_gps(distmat, wp_reid_dataset.test_info, wp_reid_dataset.probe_index, wp_reid_dataset.gallery_index,
                    wp_reid_dataset.gps_info, wp_reid_dataset.trajectory_info, k=4)

    print('TKP Duke')
    distmat = DataPacker.load(tkp_duke_dist_file)['g2g_distmat']
    update_with_gps(distmat, wp_reid_dataset.test_info, wp_reid_dataset.probe_index, wp_reid_dataset.gallery_index,
                    wp_reid_dataset.gps_info, wp_reid_dataset.trajectory_info, k=6)

    print('TKP MARS')
    distmat = DataPacker.load(tkp_mars_dist_file)['g2g_distmat']
    update_with_gps(distmat, wp_reid_dataset.test_info, wp_reid_dataset.probe_index, wp_reid_dataset.gallery_index,
                    wp_reid_dataset.gps_info, wp_reid_dataset.trajectory_info, k=4)
