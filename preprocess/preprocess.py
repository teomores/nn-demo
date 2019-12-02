import os
import time
from transform_image import transform

def process_images(source_dir, dest_dir, supported_formats=('jpeg','jpg','png')):
	"""
	Process images in the source_dir folder and save their transformations in
	the dest_dir directory.
	Each image must be located in a folder named after its category
	"""
	for root, dirs, files  in os.walk(source_dir, topdown=False):

		# assuming to work with .jpg images
		for name in [f for f in files if f.endswith(supported_formats)]:

			# create the dataset directory if it doesn't exist
			if not os.path.exists(dest_dir):
				print('Creating the dataset folder')
				os.makedirs(dest_dir)

			category = os.path.basename(os.path.normpath(root))

			# create the corresponding category directory if it doesn't exists
			if not os.path.exists(dest_dir + '/' + category):
				print('Creating the ' + category + ' category folder')
				os.makedirs(dest_dir + '/' + category)

			# process the image if it has not been already processed
			if not os.path.exists(dest_dir + '/' + category + '/' + name):
				print('Processing ' + name)
				transform(
					image_path=root + '/' + name,
					dest_dir=dest_dir + '/' + category
				)

			else:
				print(name + ' already processed')


if __name__ == '__main__':
	time_start = time.time()

	# move to the script's directory
	os.chdir(os.path.dirname(os.path.realpath(__file__)))

	process_images(
		source_dir='../data',
		dest_dir='../train/dataset'
	)
	time_end = time.time()
	print('Elasped time: %.3f sec' % (time_end - time_start))
