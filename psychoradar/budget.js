/** Budget guardrails for a future campaign manager; no external ads are modified. */
export function evaluateCampaign({ spentToday, dailyLimit, trackedCalls, spendTotal }) {
  for (const value of [spentToday, dailyLimit, trackedCalls, spendTotal]) {
    if (!Number.isFinite(value) || value < 0) throw new Error("Invalid campaign metric");
  }
  return {
    pauseRecommended: spentToday >= dailyLimit,
    costPerTrackedCall: trackedCalls > 0 ? spendTotal / trackedCalls : null,
    needsReview: trackedCalls === 0 && spendTotal > 0,
  };
}
