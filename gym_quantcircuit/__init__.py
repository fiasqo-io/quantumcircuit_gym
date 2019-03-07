from gym.envs.registration import register

register(
    id='quantcircuit-v0',
    entry_point='gym_quantcircuit.envs:QuantCircuitEnv'
)