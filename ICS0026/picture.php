<?php
  /* 
   * Encrypt and decrypt input.jpg image with AES-128-CBC
   * Author: Hannes Toots
   */
  $file = './input.jpg';

  // echo image before encryption
  echo '<p>Image before encryption:</p>
    <img src='.$file.'>';

  // encrypt
  $image = file_get_contents($file);
  $cipher = "aes-128-cbc";
  $ivlen = openssl_cipher_iv_length($cipher);
  $iv = openssl_random_pseudo_bytes($ivlen);
  $key = openssl_random_pseudo_bytes(128);
  $ciphertext = openssl_encrypt($image, $cipher, $key, $options=0, $iv);

  // print out encrypted text (debug, very long)
  // echo "Encrypted text: ".$ciphertext;

  // decrypt and display image
  $img = openssl_decrypt($ciphertext, $cipher, $key, $options=0, $iv);
  echo '<p>Decrypted image:</p>
    <img src="data:image/jpeg;base64,'.base64_encode($img).'"/>';
?>
