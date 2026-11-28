import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
namespace TubeSheets
open Complex
noncomputable def turn : ℂ := 2 * Real.pi * I
/-- On the affinely transformed seed circle the separating polynomial has
the form w * (2+w⁻¹/10)/10 with w of modulus one. -/
theorem separating_polynomial (w₁ w₂ : ℂ) :
    (1+w₁/10)^2+(I+w₂/10)^2 = (w₁+I*w₂)/10 * (2+(w₁-I*w₂)/10) := by
  linear_combination (norm := ring_nf) (1+w₂^2/100)*Complex.I_sq
/-- The explicitly lifted factor w=e^z gains 2πi per turn, while the
logarithm of the other factor has identical argument on every turn. -/
noncomputable def lift (z : ℂ) := z + Complex.log ((2 + Complex.exp (-z)/10)/10)
theorem trace (z : ℂ) (nz : (2 + Complex.exp (-z)/10)/10 ≠ 0) :
    Complex.exp (lift z) = Complex.exp z / 10 * (2 + Complex.exp (-z)/10) := by
  rw [lift,Complex.exp_add,Complex.exp_log nz]; ring
theorem increment (z : ℂ) (n : ℕ) : lift (z+n*turn) = lift z + n*turn := by
  simp only [lift,neg_add_rev,Complex.exp_add,Complex.exp_neg,turn,
    Complex.exp_nat_mul_two_pi_mul_I,inv_one,one_mul]
  ring
theorem infinitely_many_lifts (z : ℂ) : Function.Injective (fun n : ℕ => lift (z+n*turn)) := by
  intro n m eq
  simp only [increment,add_right_inj] at eq
  have nonzero : turn ≠ 0 := by simp [turn, Real.pi_ne_zero, Complex.I_ne_zero]
  exact_mod_cast (mul_right_cancel₀ nonzero eq)
/-- On the entire seed circle the second factor stays in the open right
half-plane, allowing its principal logarithm throughout the trace. -/
theorem circle_factor (θ : ℝ) : 0 < ((2 + Complex.exp (-((θ:ℂ)*I))/10)/10).re := by
  have hn : ‖Complex.exp (-((θ:ℂ)*I))‖ = 1 := by simp [Complex.norm_exp,Complex.mul_re]
  have h := Complex.abs_re_le_norm (Complex.exp (-((θ:ℂ)*I)))
  rw [hn,abs_le] at h
  simp only [Complex.div_ofNat_re,Complex.add_re]
  norm_num
  linarith [h.1]
end TubeSheets
#print axioms TubeSheets.separating_polynomial
#print axioms TubeSheets.trace
#print axioms TubeSheets.infinitely_many_lifts
#print axioms TubeSheets.circle_factor
