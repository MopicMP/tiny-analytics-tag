"""Tests for tiny-analytics-tag."""

import pytest
from tiny_analytics_tag import tag


class TestTag:
    """Test suite for tag."""

    def test_basic(self):
        """Test basic usage."""
        result = tag("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            tag("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = tag(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
