"""
--------------------------------------------------------------------------------
Copyright 2023 SiFive Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
--------------------------------------------------------------------------------

Declares the Zvfbfwma intrinsics and links to the templates for its
realization into function prototype. The documents are generated under the
sequence and grouping.
"""

from intrinsic_decorator import IntrinsicDecorators
from generator import CompatibleHeaderGenerator, APITestGenerator
from templates import mac_template
from constants import LMULS, WLMULS, NCVTLMULS

SEWS = [16]
TYPES = ["bfloat"]

llvm_header = r"""// REQUIRES: riscv-registered-target
// RUN: %clang_cc1 -triple riscv64 -target-feature +v \
// RUN:   -target-feature +zvfbfwma -disable-O0-optnone \
// RUN:   -emit-llvm %s -o - | opt -S -passes=mem2reg | \
// RUN:   FileCheck --check-prefix=CHECK-RV64 %s

"""

def gen(g):
  if isinstance(g, CompatibleHeaderGenerator):
    assert False, "Zvfbfwma intrinsics is supported after v1.0"

  if isinstance(g, APITestGenerator):
    g.set_llvm_api_test_header(llvm_header)

  decorators = IntrinsicDecorators(g.has_tail_policy)

  ####################################################################
  g.start_group("Zvfbfwma Arithmetic Intrinsics")

  g.function_group(mac_template,
                   "Vector Widening Multiply-Accumulate Intrinsics",
                   "bf16-widening-multiply-accumulate", ["wmaccbf16"], TYPES,
                   SEWS, WLMULS, decorators.has_masking_no_maskedoff_policy_frm)
