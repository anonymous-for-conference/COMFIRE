import unittest

from mutation_pipeline import normalize_unit, replace_document_span


class DocumentSpanTest(unittest.TestCase):
    def test_repeated_phrase_changes_only_selected_occurrence(self):
        source = "        language_model_keys: language_model\n"
        changed = replace_document_span(source, "language_model", "vision_tower", 2)
        self.assertEqual(changed, "        language_model_keys: vision_tower\n")
        self.assertEqual(normalize_unit(source, changed, True), changed)

    def test_missing_occurrence_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "occurrence missing"):
            replace_document_span("name: name", "name", "other", 3)

    def test_field_name_occurrence_is_rejected(self):
        source = "        language_model_keys: language_model\n"
        with self.assertRaisesRegex(ValueError, "field name"):
            replace_document_span(source, "language_model", "vision_tower", 1)
        with self.assertRaisesRegex(ValueError, "field name changed"):
            normalize_unit(source, "        vision_tower_keys: language_model\n", True)

    def test_field_directives_cannot_be_removed(self):
        source = "        :param mode: The opening mode.\n        :param encoding: Text encoding.\n"
        with self.assertRaisesRegex(ValueError, "field directives changed"):
            normalize_unit(source, source.replace(":param encoding:", "encoding:"), True)


if __name__ == "__main__":
    unittest.main()
