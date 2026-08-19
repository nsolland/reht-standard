from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompositionRule:
    """Forbidden ordered capability sequence within one governed continuity scope."""

    rule_id: str
    capabilities: tuple[str, ...]

    def __post_init__(self) -> None:
        if len(self.capabilities) < 2:
            raise ValueError("composition rule must contain at least two capabilities")


@dataclass(frozen=True)
class GovernedEffect:
    scope_ref: str
    capability: str
    action_ref: str


class CompositionClosure:
    """
    Deterministic action-history admissibility check.

    Each action can be individually authorized and still be inadmissible when
    composed with prior governed effects. History is keyed by a durable
    governed continuity scope, not by an agent/session identifier, so opening a
    new model session does not erase consequence-bearing history.
    """

    def __init__(self, rules: tuple[CompositionRule, ...] = ()) -> None:
        self.rules = rules
        self._history: dict[str, list[GovernedEffect]] = {}

    def history(self, scope_ref: str) -> tuple[GovernedEffect, ...]:
        return tuple(self._history.get(scope_ref, ()))

    def reason_codes(self, scope_ref: str, candidate_capability: str) -> tuple[str, ...]:
        prior = tuple(effect.capability for effect in self.history(scope_ref))
        proposed = prior + (candidate_capability,)
        matches = []
        for rule in self.rules:
            width = len(rule.capabilities)
            if len(proposed) >= width and proposed[-width:] == rule.capabilities:
                matches.append(f"COMPOSITION_CLOSURE:{rule.rule_id}")
        return tuple(matches)

    def admissible(self, scope_ref: str, candidate_capability: str) -> bool:
        return not self.reason_codes(scope_ref, candidate_capability)

    def record_effect(self, effect: GovernedEffect) -> None:
        self._history.setdefault(effect.scope_ref, []).append(effect)
