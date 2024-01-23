# Installing `foldx`

One of the main subset of black-boxes of `poli` relates to [`foldx`](https://foldxsuite.crg.eu/), a suite for protein design that allows you to compute, among other things, the change in free energy $dG$. This software and metric have been used as a black-box for optimization in recent work {cite:p}`stanton2022accelerating,jain:multiobjective-gflownet:2023`.

`poli` can't install `foldx` for you automatically, since the software is provided under an academic license. To install `foldx`,
1. Go to https://foldxsuite.crg.eu/
2. Download the academic license. You'll likely be downloading a zip file with the executable and auxiliary files.
3. Create a folder in your home directory called `foldx`.
4. Place your executable under `~/foldx/foldx`. You will need to rename it.
5. (If you downloaded `foldx` version 4) Make sure you have the `rotabase.txt` at `~/foldx/rotabase.txt`

If you installed everything correctly, you should be able to run
```bash
~/foldx/foldx --help
```

:::{warning}

If you are using mac, it is likely that the operating system will raise a warning about `foldx` being an unverified executable. You can remove the quarantine with the following command:

```bash
# Use at your own risk! This removes the quarantine from foldx 
xattr -d com.apple.quarantine ~/foldx/foldx
```

:::
