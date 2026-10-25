---
title: "Cost per reportable genome"
date: 2026-10-25
description: >-
  Notes from a technical briefing I gave the Pathogen Genomics Initiative team
  on choosing sequencing platforms. The instrument specification is the least
  useful number in the decision.
tags: [pathogen genomics, procurement, sequencing]
---

The question I am asked most often by laboratories planning to start sequencing
is which instrument they should buy. It is the wrong question, and answering it
directly does people a disservice.

I spent some time this year preparing a technical briefing for the Pathogen
Genomics Initiative team, built around the 2025 edition of the Front Line
Genomics *Sequencing Buyer's Guide* — a market snapshot covering extraction,
library preparation, short- and long-read platforms, and outsourcing. It is a
useful catalogue. It is also, as its own foreword states, sponsored by two
companies that sell into the market it surveys. That is not a reason to discard
it, but it is a reason to treat its comparison tables as a starting inventory
rather than as an evaluation.

Working through roughly forty platforms, the thing that struck me is how little
of the purchasing decision the specifications actually determine.

## The number that matters is downstream of the instrument

Vendors compete on output per run, read length and quality score. Q30 means an
estimated one error per thousand bases; Q40, one per ten thousand. These are
estimated per-base error probabilities. They are not the accuracy of a finished
genome, and they are certainly not the reliability of a public health
interpretation. Coverage depth cannot recover a region the assay never
amplified, and it does not correct a systematic error.

What a surveillance programme actually consumes is **reportable genomes** —
samples that pass the complete workflow and produce something a public health
decision can rest on. So the procurement metric I proposed to the team was cost
per reportable genome: total attributable workflow cost divided by the number
of samples meeting reporting criteria. It is a harder number to obtain than a
price per gigabase, because no vendor publishes it. That is rather the point.

## Where throughput goes

A worked example, with illustrative figures rather than a recommended
threshold. Take a bacterial genome of 5 Mb at 50× depth: 250 Mb of target bases
per sample. Take a run producing 15 Gb, of which perhaps 70% survives filtering
and is on-target: 10.5 Gb of effective output. That divides into about 42
samples. Ask for 100× instead and it halves to 21.

Then subtract your controls. Then account for uneven pooling, and for the
libraries that underperform. The headline capacity on a datasheet and the number
of genomes you report at the end of the month are different quantities, and the
gap between them is where budgets are lost.

## Utilisation, and the trap inside it

Fixed run costs reward filling the flow cell. A hypothetical run costing
US$1,200 works out at US$50 per sample across 24 samples, US$25 across 48, and
US$12.50 across 96. The arithmetic is seductive, and it quietly argues for
waiting until you have a full batch.

During an outbreak that argument is wrong. Waiting to fill a run converts money
saved into days lost, and days are the currency of outbreak response. Any
honest operating plan has to model both: a routine mode optimised for cost per
result, and a surge mode that accepts a half-empty flow cell.

The same realism applies to turnaround. Instrument run time is one segment of
the interval between specimen receipt and an approved report. Transport,
extraction, library preparation, queueing, transfer, analysis, QC review and
release make up the rest. A fast instrument in a slow system produces slow
reports.

## What the datasheet never covers

Site readiness decides more installations than chemistry does: power stability
and backup, environmental conditions, reagent shipping and shelf life, minimum
order quantities, replenishment lead times, trained operators, and — the one
most often discovered too late — whether the manufacturer or distributor
actually provides engineering support in the country of installation, as
distinct from the region.

Then there is the data. Versioned analysis pipelines, compute sufficient for
timely basecalling and demultiplexing, documented export of reads and metadata,
retention and access governance, and interoperability with the repositories a
programme is obliged to submit to. Deciding this after the instrument arrives is
expensive.

## Scoring, and the limits of scoring

I proposed a weighted scorecard to structure the comparison: assay fit and
demonstrated quality 30%, total cost of ownership 25%, supply and service 20%,
reporting speed and capacity 15%, data and workforce fit 10%.

The weights matter less than one rule that sits above them. Mandatory
requirements are applied *before* weighted scoring. A vendor that fails a
must-have does not get rescued by a low price or a strong total — otherwise the
scorecard becomes a mechanism for talking yourself into a bad purchase.

And the scorecard does not end the process. Acceptance criteria should be agreed
before delivery, and the pilot should run representative specimens — routine and
difficult — with proper controls, measuring QC success, reporting time,
concordance and repeat rate on complete reports rather than on vendor run
metrics.

## Not everyone needs an instrument

The last point is the one most resisted. Sequencing capacity is a network
property, not a per-laboratory badge. Predictable recurring workload justifies
in-house capacity. Low, intermittent or specialist demand often does not, and a
referral or contracted arrangement with clear terms on quality, logistics, data
return and raw-data access will serve the public health objective better than an
underused instrument with an unfunded service contract.

An instrument that sits idle is not capacity. It is a depreciating asset with a
cold chain attached.

---

*The figures above are illustrative planning arithmetic, not quotations,
benchmarks or performance guarantees. The briefing itself was prepared for
internal discussion; platform details derive from the Front Line Genomics
guide and require configuration-specific confirmation with vendors before any
procurement.*
