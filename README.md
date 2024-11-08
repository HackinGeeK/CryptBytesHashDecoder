This script decodes the SHA-1 hash output from the Java cryptBytes function, which is commonly used in certain Java applications for hashing sensitive data. The tool extracts and converts the hash into a format compatible with popular hash-cracking tools like John the Ripper (JtR) and Hashcat.

Overview
The Java cryptBytes function is used to generate hashes of the format $SHA$salt$base64hash, where:

*/ $SHA$ indicates the hash algorithm used (typically SHA-1 by default).
*/ salt is a randomly generated value appended to the data to prevent hash collisions for identical inputs.
*/ base64hash is the base64-encoded result of the SHA-1 hash function applied to the input data with the specified salt.
