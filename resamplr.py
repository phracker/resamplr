#!/usr/bin/env python
# -*- coding: utf-8 -*-
# resamplr.py: Intelligently resample FLACs
VERSION='0.2'

import os, sys, subprocess, re, glob, errno, logging, argparse
import sox

logging.basicConfig(level=logging.WARN)

def get_target_sample_rate(file_name):
  in_sr = sox.file_info.sample_rate(file_name)
  out_sr = 0
  if (int(in_sr) % 44100) == 0:
    out_sr = 44100
  elif (int(in_sr) % 48000) == 0:
    out_sr = 48000
  else:
    raise Exception()
  return out_sr

def resample_file(file_name,out_dir,out_sample_rate=0,out_bit_depth=16):
  out_file_name = os.path.join(out_dir,os.path.basename(file_name))
  if out_sample_rate == 0:
    out_sample_rate = get_target_sample_rate(file_name)
  logging.info('Converting... ( input: {}, output: {}, samplerate: {}, bitdepth: {} )'.format(file_name,out_file_name,out_sample_rate,out_bit_depth))
  tfm = sox.Transformer()
  tfm.convert(samplerate=out_sample_rate,bitdepth=out_bit_depth)
  tfm.build(file_name,out_file_name)

def get_flacs(dir_path):
  flacs = []
  for root, dirs, files in os.walk(dir_path):
    for f in files:
      if f.endswith('.flac'):
        flacs.append(os.path.realpath(os.path.join(root,f)))
  return flacs

def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as exc:  # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass
    else:
      raise

if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='resamplr',description='Resample FLACs intelligently.')
  parser.add_argument('-v','--version',action='version',version='%(prog)s {}'.format(VERSION))
  parser.add_argument('source',help='Directory of FLACs to resample.')
  parser.add_argument('dest',help='Destination directory for resampled FLACs.')
  parser.add_argument('--bitdepth','-b',default=16,type=int,help='Desired bit depth for resampled FLACs. Default: 16')
  parser.add_argument('--samplerate','-s',default=0,type=int,help='Desired samplerate for resampled FLACs. Default: Automatically selects 44100 or 48000 based on input files')
  args = parser.parse_args()

  in_directory = args.source
  logging.info('in_directory: {}'.format(in_directory))
  in_flacs = get_flacs(in_directory)
  logging.info('in_flacs: {}'.format(str(in_flacs)))
  out_sample_rate = args.samplerate
  logging.info('out_sample_rate: {}'.format(out_sample_rate))
  out_bit_depth = args.bitdepth
  logging.info('out_bit_depth: {}'.format(out_bit_depth))
  out_directory = args.dest
  logging.info('out_directory: {}'.format(out_directory))
  logging.info('Creating out_directory...')
  mkdir_p(out_directory)
  logging.info('Beginning resampling process...')
  for flacfile in in_flacs:
    logging.info('Working on {}'.format(flacfile))
    resample_file(flacfile,out_directory,out_sample_rate=out_sample_rate,out_bit_depth=out_bit_depth)
  logging.info('Done!')
