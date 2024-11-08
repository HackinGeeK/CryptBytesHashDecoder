import base64
import argparse

def process_hash(hash_input):
    # Strip the hash type ($SHA$) and the salt ($d$)
    _, hash_type, salt, base64_url_hash = hash_input.split('$')

    # Adjust the base64-url encoded string to add padding if necessary
    padding_adjusted_hash = base64_url_hash + '=' * ((4 - len(base64_url_hash) % 4) % 4)

    # Decode from base64-url with adjusted padding
    decoded_bytes = base64.urlsafe_b64decode(padding_adjusted_hash)

    # Encode as hex
    hex_encoded = decoded_bytes.hex()

    # Append the salt to the final hex value, separated by a colon
    final_result = f"{hex_encoded}:{salt}"
    return final_result

# Setup argparse to get the hash input from the command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a hash and output hex with salt.")
    parser.add_argument("hash_input", type=str, help="The hash input in the format $SHA$salt$base64hash")
    args = parser.parse_args()

    # Process the hash and print the result
    print(process_hash(args.hash_input))