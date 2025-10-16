import argparse
import logging
from utils import load_config
from pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="Run OCR preprocessing pipeline on a folder of images.")
    parser.add_argument("image_dir", help="Path to input image directory containing JPEG files.")
    parser.add_argument("--config", dest="config_path", default="preprocessing/configs/base.yaml",
                        help="Path to YAML configuration file.")
    args = parser.parse_args()
    # Load configuration
    config = load_config(args.config_path)
    # Configure logging (console and file)
    log_level = config.get('logging', {}).get('level', 'INFO').upper()
    log_file = config.get('logging', {}).get('file', 'pipeline.log')
    logging.basicConfig(level=getattr(logging, log_level, logging.INFO),
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(log_file), logging.StreamHandler()])
    logging.info("Starting OCR preprocessing pipeline...")
    # Run pipeline
    run_pipeline(args.image_dir, config)

if __name__ == "__main__":
    main()
