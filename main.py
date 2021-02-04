import argparse
import torch
from train import cycleGAN

def Arguments():
    parser = argparse.ArgumentParser(description='Arguments for CycleGAN.')

    parser.add_argument('--gpu', type=int, default=6, help='GPU number to use.')
    # Dataset arguments
    parser.add_argument('--dataset_path', type=str, default='/mnt/hdd/LJJ/DATA/pix2pix/concat', help='Dataset file path.')
    parser.add_argument('--batch_size', type=int, default=8, help='Integer value for batch size.')
    parser.add_argument('--image_size', type=int, default=256, help='Integer value for number of points.')
    parser.add_argument('--input_nc', type=int, default=3, help='size of image height')
    parser.add_argument('--output_nc', type=int, default=3, help='size of image height')
    parser.add_argument('--channels', type=int, default=10, help='Number of image channels')
    
    # Optimizer arguments
    parser.add_argument('--b1', type=int, default=0.5, help='GPU number to use.')
    parser.add_argument('--b2', type=int, default=0.999, help='GPU number to use.')
    parser.add_argument('--lr', type=float, default=2e-4, help='Adam : learning rate.')
    parser.add_argument('--decay_epoch', type=int, default=100, help="epoch from which to start lr decay")

    # Training arguments
    parser.add_argument('--epoch', type=int, default=0, help='Epoch to start training from.')
    parser.add_argument('--num_epochs', type=int, default=200, help='Number of epochs of training.')
    parser.add_argument('--root_path', type=str, default='/mnt/hdd/LJJ/GAN/cycleGAN/datasets/apple2orange/', help='Checkpoint path.')
    parser.add_argument('--ckpt_path', type=str, default='/mnt/hdd/LJJ/GAN/ckpt/', help='Checkpoint path.')
    parser.add_argument('--result_path', type=str, default='/mnt/hdd_10tb_1/LJJ/DCGAN/save/generated/', help='Generated results path.')
    parser.add_argument('--sample_interval', type=int, default=20, help='Interval between sampling of images from generators')
    parser.add_argument("--checkpoint_interval", type=int, default=1, help="interval between model checkpoints")
    
    # Network arguments
    parser.add_argument('--lambdaGP', type=int, default=10, help='Lambda for GP term.')
    parser.add_argument('--latent', type=int, default=64, help='random latent size')
    parser.add_argument('--hidden', type=int, default=256, help='hidden layer size')
    
    # Model arguments
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = Arguments()

    args.device = torch.device('cuda:'+str(args.gpu) if torch.cuda.is_available() else 'cpu')

    model = cycleGAN(args)
    
    model.run(save_ckpt=args.ckpt_path, result_path=args.result_path)
 
