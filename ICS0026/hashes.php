<!DOCTYPE html>
<?php
/* Hashes strings in $arrstrings based on current algorithm in $arralgos,
 * prints the outcome and shows WALL CLOCK time, which is not just cpu time,
 * but is good enough for this test.
 * Micro time can show 0 because of how little time it takes to hash
 * given strings.
 * Author: Hannes Toots
 */

// print values in $arrstrings hashed with $arralgos
function printValues($arralgos, $arrstrings, $key) {
  $algolength = count($arralgos);
  $stringlength = count($arrstrings);
  for ($x = 0; $x < $algolength; $x++) {
    for($y = 0; $y < $stringlength; $y++) {
      echo "<p> Algo: ".$arralgos[$x]." <br/>String: ".$arrstrings[$y]." <br/>Key: ".$key."</p>";
      // just for fun, we will also get wall clock time here
      $tstart = microtime(true);
      $result = hash($arralgos[$x], $key.$arrstrings[$y]);
      $tend = microtime(true);
      $timeTook = $tend - $tstart;
      echo "<p> Result: ".$result."</p>";
      echo '<p>Hash exec <b>in wall clock</b>: '.$timeTook.' seconds</p>';
      echo "<br/>";
    }
  }
}

$key = "aaaabbbbccccdddd";
$arralgos = array("md5", "sha1", "sha256");
$arrstrings = array("The red fox jumps over the blue dog", "The red fox jumps ouer the blue dog", "The red fox jumps oevr the blue dog", "The red fox jumps oer the blue dog");

printValues($arralgos, $arrstrings, $key);
?>
